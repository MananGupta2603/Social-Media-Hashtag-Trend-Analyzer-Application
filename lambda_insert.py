import json
import boto3
import uuid
import re  

# Initialize DynamoDB resource and specify table name
dynamodb = boto3.resource('dynamodb')
table_name = 'HashtagsTable'  # Replace with your actual DynamoDB table name
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    try:
        # Extract post_content from event
        body = json.loads(event['body'])
        post_content = body['post_content']

        # Extract hashtags using regex for more precise extraction
        hashtags = re.findall(r'#(\w+)', post_content)
        
        # Check if hashtags are found
        if not hashtags:
            return {
                'statusCode': 400,
                'body': ('No hashtags found in the post content'),
                
            }

        # Generate a unique ID for each hashtag item
        for hashtag in hashtags:
            item_id = str(uuid.uuid4())  # Generate a unique ID for each item
            # Store data into DynamoDB for each hashtag
            response = table.put_item(
                Item={
                    'item_id': item_id,
                    'hashtag': hashtag,
                    'text':post_content,
                    # Add other attributes as needed based on your application's requirements
                }
            )

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Data stored successfully'}),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)}),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        }

import json
import boto3

# Initialize DynamoDB resource and specify table name
dynamodb = boto3.resource('dynamodb')
table_name = 'HashtagsTable'  # Replace with your actual DynamoDB table name
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    try:
        # Use ProjectionExpression to specify the attributes you want to retrieve
        response = table.scan(
            ProjectionExpression='hashtag'
        )
        data = response.get('Items', [])
        
        # Ensure all items have the same keys
        for item in data:
            if 'item_id' not in item:
                item['item_id'] = None
            if 'hashtag' not in item:
                item['hashtag'] = None
        
        return {
            'statusCode': 200,
            'body': json.dumps(data),
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

# Social Media Hashtag Trend Analyzer Application

## Overview
The Social Media Hashtag Trend Analyzer is a web application that analyzes trends in hashtags from social media posts. The application is built using Python, SQL, AWS Lambda, DynamoDB, and Streamlit. It allows users to input social media posts, extract hashtags, store them in a DynamoDB table, and visualize trending hashtags over time.

## Features
- **Post Input**: Users can input social media posts into the application.
- **Hashtag Extraction**: The application extracts hashtags from the posts using regular expressions.
- **Data Storage**: Hashtags and their associated post content are stored in a DynamoDB table.
- **Trend Analysis**: Analyze the frequency and trends of different hashtags over time.
- **Visualization**: Visualize trending hashtags using Streamlit.

## Technologies Used
- **Python**: The main programming language used for the backend logic and data processing.
- **SQL**: Used for querying and analyzing data (if applicable).
- **AWS Lambda**: Serverless functions to handle backend processing and data storage.
- **DynamoDB**: NoSQL database to store hashtags and post content.
- **Streamlit**: A Python library used to create the web interface for the application.

## Architecture
1. **User Input**: Users input their social media posts through the Streamlit web interface.
2. **AWS Lambda**: The input is sent to an AWS Lambda function that extracts hashtags and stores them in DynamoDB.
3. **DynamoDB**: Stores the extracted hashtags along with their associated post content.
4. **Visualization**: Streamlit retrieves data from DynamoDB and visualizes the trending hashtags.

## Setup and Installation

### Prerequisites
- Python 3.8 or higher
- AWS account with DynamoDB and Lambda services enabled
- AWS CLI configured with appropriate credentials
- Streamlit

### Installation Steps
1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/social-media-hashtag-trend-analyzer.git
    cd social-media-hashtag-trend-analyzer
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up AWS Lambda Function**:
    - Create a Lambda function in AWS Management Console.
    - Set the runtime to Python 3.8.
    - Copy the contents of `lambda_function.py` from this repository to the Lambda function.
    - Configure the Lambda function to have permissions to write to DynamoDB.

4. **Create DynamoDB Table**:
    - Create a table named `HashtagsTable` with `item_id` as the partition key (String).

5. **Run Streamlit Application**:
    ```bash
    streamlit run app.py
    ```

## Usage
1. Open the Streamlit web application in your browser.
2. Input your social media post in the provided text box.
3. Submit the post to see the extracted hashtags stored in DynamoDB.
4. View trending hashtags visualized on the web interface.

## Project Structure
social-media-hashtag-trend-analyzer/
```
   lambda_function.py # AWS Lambda function code
   app.py # Streamlit application code
requirements.txt # Python dependencies
 README.md # Project documentation
```

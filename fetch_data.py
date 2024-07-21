import streamlit as st
import requests

# Define API endpoint for Lambda function
API_ENDPOINT = 'https://cpgzsy87yk.execute-api.ap-south-1.amazonaws.com/my_fetch_lambda'


# Streamlit UI
st.title('Social Media Hashtag Viewer')

if st.button('Fetch Hashtags'):
    try:
        response = requests.get(API_ENDPOINT)
        if response.status_code == 200:
            data = response.json()
            if data:
                st.success('Data fetched successfully!')
                
                # Extract only the 'hashtag' attribute from each item
                hashtags = [item.get('hashtag', 'N/A') for item in data]
                
                # Display the hashtags as a list
                st.write("List of Hashtags:")
                for hashtag in hashtags:
                    st.write(hashtag)
            else:
                st.warning('No data found.')
        else:
            st.error(f'Failed to fetch data. Error: {response.text}')
    except requests.exceptions.RequestException as e:
        st.error(f'Error connecting to API Gateway: {e}')
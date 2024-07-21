import streamlit as st
import requests
from collections import Counter
import time


# Define API endpoints
API_ENDPOINT_POST = 'https://kdoiogam58.execute-api.us-east-1.amazonaws.com/my_lambda'
API_ENDPOINT_FETCH = 'https://3gsqstb2nd.execute-api.us-east-1.amazonaws.com/my_fetch_lambda'

# Streamlit UI configuration
st.set_page_config(page_title='Social Media Dashboard', layout='centered')

# Main container for the social media layout
st.title('Social Media Dashboard')
st.markdown("---")


# Center aligning the main content
main_column = st.container()
with main_column:
    # Post composer section
    st.subheader('Create a Post')
    post_content = st.text_area('Write your post here:', height=150, placeholder='Write here!', max_chars=200)
    publish_button = st.button('Publish 🚀')  

    if publish_button:
        with st.spinner('Publishing...'):
            time.sleep(2)
            if post_content:
                payload = {'post_content': post_content}
                try:
                    response = requests.post(API_ENDPOINT_POST, json=payload)
                    if response.status_code == 200:
                        st.success('Post published successfully! 🎉') 
                        
                    else:
                        st.error(f"Failed to publish post. Error: {response.text}")
                except requests.exceptions.RequestException as e:
                    st.error(f"Error connecting to API Gateway: {e}")
            else:
                st.warning('Please write something before publishing.')
    
    st.markdown("---")

    # Top Hashtags section
    st.subheader('Trending Hashtags')
    fetch_button = st.button('Show Trending Hashtags 🔍')  

    if fetch_button:
        with st.spinner('Fetching hashtags...'):
            time.sleep(2)
            try:
                response = requests.get(API_ENDPOINT_FETCH)
                if response.status_code == 200:
                    data = response.json()
                    if data:
                        st.success('Data fetched successfully! ✅')  
                        # Extract and count hashtags
                        all_hashtags = [item.get('hashtag', 'N/A') for item in data]
                        hashtag_counts = Counter(all_hashtags)
                        top_10_hashtags = hashtag_counts.most_common(10)
                        # Display top 10 hashtags
                        for idx, (hashtag, count) in enumerate(top_10_hashtags, 1):
                            st.write(f"{idx}. #{hashtag}")
                    else:
                        st.warning('No data found.')
                else:
                    st.error(f'Failed to fetch data. Error: {response.text}')
            except requests.exceptions.RequestException as e:
                st.error(f'Error connecting to API Gateway: {e}')

    st.markdown("---")

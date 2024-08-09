import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

api_url_user = os.getenv('API_URL_USER')
api_url_link = os.getenv('API_URL_LINK')
api_key = os.getenv('API_KEY')

post_data = {
    'key': api_key
}

response_user = requests.post(api_url_user, data=post_data)
credentials_list = response_user.json()

with open('data.json', 'w') as file:
    json.dump(credentials_list, file, indent=4)

response_link = requests.post(api_url_link, data=post_data)
urls = response_link.json()

with open('data_url.json', 'w') as file:
    json.dump(urls, file, indent=4)

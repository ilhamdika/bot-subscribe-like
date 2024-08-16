import requests
import json
import os
from dotenv import load_dotenv
from getpass import getpass
import sys

load_dotenv()

base_url = os.getenv('BASE_URL')
api_key = os.getenv('API_KEY')

username = input("Masukkan username: ")
password = getpass("Masukkan password: ")

api_url_user = base_url + '/api/getShit'
api_url_link = base_url + '/api/getUrl'

post_data = {
    'key': api_key,
}

post_data_url = {
    'key': api_key,
    'username': username,
    'password': password
}

try:
    response_user = requests.post(api_url_user, data=post_data)
    response_user.raise_for_status()
    credentials_list = response_user.json()

    with open('data.json', 'w') as file:
        json.dump(credentials_list, file, indent=4)

    response_link = requests.post(api_url_link, data=post_data_url)
    response_link.raise_for_status()
    urls = response_link.json()

    if 'error' in urls:
        print(f"Error: {urls['error']}")
        with open('data.json', 'w') as file:
            file.write('[]')
        with open('data_url.json', 'w') as file:
            file.write('[]')
        sys.exit(1) 

    with open('data_url.json', 'w') as file:
        json.dump(urls, file, indent=4)

    print("Get data berhasil")
    sys.exit(0)

except requests.exceptions.HTTPError as http_err:
    print(f"password salah")
    with open('data.json', 'w') as file:
        file.write('[]')
    with open('data_url.json', 'w') as file:
        file.write('[]')
    sys.exit(1)

except Exception as err:
    print(f"An error occurred: {err}")
    with open('data.json', 'w') as file:
        file.write('[]')
    with open('data_url.json', 'w') as file:
        file.write('[]')
    sys.exit(1)
import requests
import logging
from os import getenv
from dotenv import load_dotenv

load_dotenv()
BASE_URL = getenv('BASE_URL')

def create_post(title, description, file=None):
    data = {'title': title, 'description': description}
    files = {'file': file} if file else None
    
    response = requests.post(f"{BASE_URL}", data=data, files=files)
    
    return response
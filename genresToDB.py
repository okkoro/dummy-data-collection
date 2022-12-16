import requests
from dotenv import load_dotenv
import os
import firebase_admin
from firebase_admin import firestore, credentials

load_dotenv()

api_link = os.environ.get("API_LINK")
api_key = os.environ.get("API_KEY")
db_key_path = os.environ.get("DB_KEY_PATH")

cred = credentials.Certificate(f"{db_key_path}")
app = firebase_admin.initialize_app(cred)
db = firestore.client()

response = requests.get(f"{api_link}genre/movie/list?api_key={api_key}&language=en-US")

print(response.json())

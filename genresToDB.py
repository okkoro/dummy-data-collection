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

requestLink = f"{api_link}/genre/movie/list?api_key={api_key}&language=en-US"

response = requests.get(requestLink).json()["genres"]

for genre in response:
    ref = db.collection(u"genres").document(str(genre['id']))

    ref.set(genre)

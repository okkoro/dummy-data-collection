import requests
from dotenv import load_dotenv
import os
import firebase_admin
from firebase_admin import firestore, credentials

load_dotenv()

api_link = os.environ.get("API_LINK")
api_key = os.environ.get("API_KEY")
db_key_path = os.environ.get("DB_KEY_PATH")

# response is the array of movies

# Drop everything we don't need
# Feed the array back with only needed info
cred = credentials.Certificate(f"{db_key_path}")
app = firebase_admin.initialize_app(cred)
db = firestore.client()

page = 1

while page <= 500:
    response = requests.get(f"{api_link}/top_rated?api_key={api_key}&language=en-US&page={page}").json()["results"]

    if page == 1:
        page -= 1

    page += 10

    for movie in response:
        del movie['adult']
        del movie['backdrop_path']
        del movie['original_title']
        del movie['popularity']
        del movie['video']
        del movie['vote_count']

        ref = db.collection(u"movies").document(str(movie['id']))

        ref.set(movie)

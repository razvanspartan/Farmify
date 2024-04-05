import firebase_admin
from firebase_admin import credentials

class FirebaseRepo:
    def __init__(self):
        self.__cred = credentials.Certificate("farmify-3ad30-firebase-adminsdk-y9fj0-d6fb48051c.json")
        firebase_admin.initialize_app(self.__cred)


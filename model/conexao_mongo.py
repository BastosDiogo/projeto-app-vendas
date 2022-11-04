import os
from dotenv import load_dotenv

import pymongo

load_dotenv()

class Pymongo:
    def __init__(self) -> None:
        MONGO_HOST = os.getenv("MONGO_HOST")
        MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
        MONGO_USERNAME = os.getenv("MONGO_USERNAME")
        self.client = pymongo.MongoClient(
            f"mongodb+srv://{MONGO_USERNAME}:{MONGO_PASSWORD}{MONGO_HOST}",
            tls=True,
            tlsCAFile="isrgrootx1.pem",
            tlsAllowInvalidHostnames=True,
            retryWrites=False,)
        self.database = self.client[os.getenv("DATABASE_ENVIROMENT")]
        #self.database = self.client[os.getenv("DATABASE_ENVIROMENT")]['candidato']



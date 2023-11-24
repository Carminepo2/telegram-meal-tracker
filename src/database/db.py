import certifi
import pymongo

from configs.env import ENV

mongo_client = pymongo.MongoClient(
    ENV.MONGODB_CONNECTION_STRING, tlsCAFile=certifi.where()
)

db = mongo_client[ENV.MONGODB_DATABASE_NAME]

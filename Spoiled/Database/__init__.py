from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
from config import DATABASE

mongo = MongoClient(DATABASE.MONGO_DB_URL)

db = mongo.SPL

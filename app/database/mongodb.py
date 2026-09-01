from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

client = AsyncIOMotorClient(settings.MONGODB_URL)
database = client[settings.MONGODB_DATABASE]


def get_database():
    return database


def get_collection(name: str):
    return database[name]
from typing import Dict, Union
from motor.motor_asyncio import AsyncIOMotorClient as MongoCli
from async_pymongo import AsyncClient
from MukeshRobot import MONGO_DB_URI

mongo = MongoCli(MONGO_DB_URI)
name = mongo.MukeshRobot

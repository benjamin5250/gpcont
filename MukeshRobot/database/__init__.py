from async_pymongo import AsyncClient
from typing import Dict, Union
from motor.motor_asyncio import AsyncIOMotorClient as MongoCli
from MukeshRobot import MONGO_DB_URI

mongo = MongoCli(MONGO_DB_URI)
dbname = mongo.MukeshRobot

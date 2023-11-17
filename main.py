from dotenv import load_dotenv, find_dotenv
import os
import pprint
from pymongo import MongoClient
load_dotenv(find_dotenv()) #to load the .env file so you don't have to define the path

password = os.environ.get("MONGODB_PWD")

connection_string = f"mongodb+srv://emmanuella:{password}@cen-pythoncrudapp.chbox2f.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(connection_string)
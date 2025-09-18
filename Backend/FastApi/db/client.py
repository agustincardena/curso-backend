from pymongo import MongoClient

#Base de datos local
#db_client = MongoClient().local

#Base de datos remota

db_client= MongoClient(
    "mongodb+srv://agustincardena_db_user:t5TWspeQJ3DIRU6c@cluster0.15kow2b.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0").cluster0
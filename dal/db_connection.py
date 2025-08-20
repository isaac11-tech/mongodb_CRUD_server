from pymongo import MongoClient
import os


class ConnectionDB:
    def __init__(self, db_name, collection_name):
        mongo_host = os.getenv("MONGO_HOST")
        mongo_port = os.getenv("MONGO_PORT")
        mongo_user = os.getenv("MONGO_USER")
        mongo_pass = os.getenv("MONGO_PASS")

        uri = f"mongodb://{mongo_user}:{mongo_pass}@{mongo_host}:{mongo_port}/"

        # connecting to server
        self.client = MongoClient(uri)
        # select a DB
        self.db = self.client[db_name]
        # select collection
        self.collection = self.db[collection_name]


    #INSERT
    def insert_collection(self, document_data: dict):
        try:
          result = self.collection.insert_one(document_data)
          return str(result.inserted_id)
        except Exception as e:
          return {"success": False, "error": str(e)}

    # READ
    def get_all_collection(self):
        try:
          return list(self.collection.find({}, {"_id": 0}))
        except Exception as e:
          return {"success": False, "error": str(e)}


    # UPDATE
    def update_collection(self, document_id: int, update_fields: dict):
        try:
          result = self.collection.update_one({"ID": document_id}, {"$set": update_fields})
          return result.modified_count > 0
        except Exception as e:
          return {"success": False, "error": str(e)}

    # DELETE
    def delete_collection(self, document_id: int):
        try:
          result = self.collection.delete_one({"ID": document_id})
          return result.deleted_count > 0
        except Exception as e:
          return {"success": False, "error": str(e)}

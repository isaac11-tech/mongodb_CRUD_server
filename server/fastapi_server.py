from fastapi import FastAPI
from dal.db_connection import ConnectionDB

app = FastAPI()


db = ConnectionDB(db_name="mydb", collection_name="soldiers")


@app.post("/insert_data")
def insert_data(document_data: dict):
    return db.insert_collection(document_data)


@app.get("/get_collection")
def get_collection():
    return db.get_all_collection()

@app.post("/update")
def update_collection(document_id: int, update_fields: dict):
    return db.update_collection(document_id,update_fields)

@app.delete("/delete")
def delete_collection(document_id: int):
    return db.delete_collection(document_id)



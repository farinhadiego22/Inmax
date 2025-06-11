from fastapi import FastAPI
from db import get_db

app = FastAPI()

@app.get("/")
def root():
    return {"msg": "FastAPI conectado"}

@app.get("/test-db")
def test_db():
    db = get_db()
    test_col = db["test"]
    test_doc = {"mensaje": "Hola desde Mongo!"}
    
    if test_col.count_documents({}) == 0:
        test_col.insert_one(test_doc)
    
    docs = list(test_col.find({}, {"_id": 0}))
    return {"documentos": docs}


@app.get("/test2-db")
def test_db():
    db = get_db()
    test_col = db["test2"]
    test_doc = {"mensaje": "Hola desde Mongo2!"}
    
    if test_col.count_documents({}) == 0:
        test_col.insert_one(test_doc)
    
    docs = list(test_col.find({}, {"_id": 0}))
    return {"documentos": docs}

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pymongo
from random import random
from telergam import send_order_to_telegram


mongo_addres = 'mongodb://localhost:27017'
db_client = pymongo.MongoClient(mongo_addres)
db = db_client['orders_db']
order_collection = db['order']

app = FastAPI()

origins = [
    "http://localhost:3000",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class OrderModel(BaseModel):
    order: dict

@app.get('/')
def get():
    # order_collection.insert_one({"number": 1, "code": 2, "data": 3})
    return {"status": "ok:)"}


@app.post('/set/order')
async def recive_order(data: OrderModel):
    data.order['id'] = int(random() * 100000000)
    await send_order_to_telegram(data.order)
    order_collection.insert_one({"order": data.order})
    return {"status": 200}
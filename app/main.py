from fastapi import FastAPI
from pymongo import MongoClient
import uvicorn
from producer import produce_user_update

app = FastAPI()

client = MongoClient('mongodb://localhost:27017/')
db = client['user_db']
users_collection = db['users']

@app.post("/user/update")
async def update_user(user: dict):
    # Update MongoDB
    # users_collection.update_one(
    #     {'user_id': user['user_id']},
    #     {'$set': user},
    #     upsert=True
    # )
    print("Passing data into producer to update User Details")
    # Produce Kafka message
    produce_user_update(user)

    return {"message": "User updated and event produced to Kafka"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

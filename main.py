import uvicorn
from fastapi import FastAPI

app = FastAPI()

users=[
    {
        "id": 1,
        "username": "admin",
        "email": "admin@localhost",
        "password": "admin123",
    },
    {
        "id": 2,
        "username": "user",
        "email": "user@localhost",
        "password": "user123",
    }
]

@app.get("/users")
def get_users():
    return users

@app.get("/user_by_id/{id}")
def get_users2(id:int):
    return users[id]

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
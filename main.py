import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
def get_users():
    return [{"id":1,"name":"Some","email":"Some"}]

@app.get("/users")
def get_users2():
    return [{"id":1,"name":"Some","email":"Some"}]

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
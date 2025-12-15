from fastapi import FastAPI, Body
import uvicorn
from pydantic import EmailStr, BaseModel

app = FastAPI()


class CreateUser(BaseModel):
    email: EmailStr


@app.get("/")
def hello_index():
    return {"message": "Hello Index"}


@app.get("/items")
def list_items():
    return ["item_id1", "item_id2"]


@app.get("/items/{item_id}")
def get_item_by_id(item_id: int):
    return {"item_id": item_id}


@app.post("/users")
def create_user(user: CreateUser):
    return {"message": "User created", "email": user.email}


@app.post("/calc/add")
def add(num1: int, num2: int):
    return {"result": num1 + num2}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

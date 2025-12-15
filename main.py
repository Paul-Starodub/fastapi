from fastapi import FastAPI
import uvicorn
from pydantic import EmailStr, BaseModel
from items_views import router as items_router

app = FastAPI()
app.include_router(items_router)


class CreateUser(BaseModel):
    email: EmailStr


@app.get("/")
def hello_index():
    return {"message": "Hello Index"}


@app.post("/users")
def create_user(user: CreateUser):
    return {"message": "User created", "email": user.email}


@app.post("/calc/add")
def add(num1: int, num2: int):
    return {"result": num1 + num2}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

from fastapi import FastAPI
from pydantic import BaseModel

# Create the FastAPI app
app = FastAPI()

# Define request body using Pydantic model
class Numbers(BaseModel):
    num1: float
    num2: float

# POST endpoint at /add
@app.post("/add")
def add_numbers(data: Numbers):
    return {"received": {"num1": data.num1, "num2": data.num2,"sum": data.num1 + data.num2}}


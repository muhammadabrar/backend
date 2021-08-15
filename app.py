from fastapi import FastAPI
from pydantic import BaseModel
#  an HTTP-specific exception class  to generate exception information
from fastapi.middleware.cors import CORSMiddleware

#config app
app = FastAPI()
origins = [
    "http://localhost:3000",
]

# middleware? 

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None


@app.get("/")
async def root():
    return {"I": "am Abrar"}


@app.get("/api/{title}")
async def getTile(title):
    Title = title
    if Title:
        return Title



@app.post("/items/")
async def create_item(item: Item):
    return item

#localhost:8000/docs

# step1: create rep
# git init
# git remote add origin https://github.com/muhammadabrar/ecu_priamry.git
# git add .
# git commit -m initial
# git branch -M main
# git push -u origin main
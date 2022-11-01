from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import Optional

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from Transactions.SalesData import Sales_Order

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# open bds in terminal

# https://qemtgmilflgbhgrhnmdx.supabase.co
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFlbXRnbWlsZmxnYmhncmhubWR4Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY2NjI0ODUyOCwiZXhwIjoxOTgxODI0NTI4fQ.E9ZkTW2dKolRSTjMSlAbFBbkbbKf-huq8WAzzOy5GlM


@app.get("/salesorder/{id}")
async def read_sales_order(id: int):
    print(id)
    return Sales_Order(id)



class Item(BaseModel):
    username: str
    empSatisfaction: float
    email: str
    score: int


class personID(BaseModel):
    id: int


class messageSchema(BaseModel):
    message: str


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/")
async def read_root(item: Item):  # item is posted value
    print(item)
    return {"Hello": "World"}




# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: Optional[str] = None):
#    return {"item_id": item_id, "q": q}


# @app.get("/recommendation")
# async def Recommendation_item(person_id: personID):
#     return recommendation(person_id)
#
#
# @app.get("/recommendation/{id}")
# async def Recommendation_item(id: int):
#     print(id)
#     return recommendation(id)


## Product Search API
#                                     name: name,
#                                     brand: brand,
#                                     priceMin: priceMin,
#                                     priceMax: priceMax,
#                                     rating: rating,
#                                     color: color,
#                                     gender: gender
#                                     category: category

# @app.get("/search")
# async def Search(name: str = "", brand: str = "", priceMin: float = 0.0, priceMax: float = 999999.99,
#                  rating: float = 0.0, color: str = "", gender: str = "", category: str = ""):
#     return search(name, brand, priceMin, priceMax, rating, color, gender, category)


# pip freeze > requirements.txt
# pip install -r requirements.txt
# uvicorn main:app --reload

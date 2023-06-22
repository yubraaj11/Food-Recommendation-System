from fastapi import FastAPI
from Recommendation import recommendation

app = FastAPI()


@app.get("/")
def read_root():
    return {"Food": "Recommendation"}



@app.get("/foodRecSys")
def food_rec(day: int, hour: int): # query parameters
    product_name = recommendation(day=day, hour=hour)
    for items in product_name:
        return items
    # return {"message": "Items printed successfully"}

        
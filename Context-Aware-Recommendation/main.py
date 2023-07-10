from fastapi import FastAPI
from Recommendation import recommendation
# from evaluation import eval_metrics
app = FastAPI()


@app.get("/")
def read_root():
    return {"Food": "Recommendation"}


@app.get("/foodRecSys")
def food_rec(day: int, hour: int): # query parameters
    """
    Recommends food products based on the given day and hour.

    Args:
        day (int): The day for which recommendations are desired.
        hour (int): The hour of the day for which recommendations are desired.

    Yields:
        str: A food product name recommended based on the given day and hour.
    """
    product_name = recommendation(day=day, hour=hour)
    # return {"product_names": product_name}
    for items in product_name:
        yield items


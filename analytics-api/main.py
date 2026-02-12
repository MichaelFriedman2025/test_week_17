from fastapi import FastAPI
import uvicorn
from dal import *


app = FastAPI()


@app.get("/analytics/top-customers")
def get_ten_costumers():
    res = ten_costumers_with_high_order()
    return {"res":[res]}

@app.get("/analytics/customers-without-orders")
def get_all_costumers_without_orders():
    pass

@app.get("/analytics/zero-credit-active-customers")
def get_all_costumers_with_ziro_limit_card():
    pass

if __name__=="__main__":
    uvicorn.run("main:app",host="127.0.0.1",port= 8000) 
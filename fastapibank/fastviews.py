"""
api to use bank
"""


#from flask import Blueprint, render_template, request, jsonify, redirect, url_for
import fastapi
from main import accountManagment, atm

from fastapi import FastAPI, Path, Query, HTTPException, status

app = FastAPI()


@app.get("/getCash/byName/{customer_name}")
def get_cash(customer_name: str = Path(description="The name of the customer, to get his/her money.", gt=0)):
    cash_amount = atm.getCashAmountByName(customer_name)

    if cash_amount == -1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return cash_amount


@app.get("/getCash/byId/{customer_id}")
def get_cash(customer_id: int = Path(description="The ID of the customer, to get his/her money.", gt=0)):
    cash_amount = atm.getCashAmountById(customer_id)

    if cash_amount == -1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return cash_amount


@app.put("/deposit/{customer_id}/{cash_amount}")
def deposit(customer_id: int, cash_amount: int):
    if atm.deposit(customer_id, cash_amount):
        raise HTTPException(status_code=status.HTTP_200_OK)
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    

@app.put("/withdraw/{customer_id}/{cash_amount}")
def deposit(customer_id: int, cash_amount: int):
    if atm.withdraw(customer_id, cash_amount):
        raise HTTPException(status_code=status.HTTP_200_OK)
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    

@app.put("/send/{customer_id}/{cash_amount}/{taker_id}")
def deposit(customer_id: int, cash_amount: int, taker_id: int):
    if atm.send(customer_id, cash_amount, taker_id):
        raise HTTPException(status_code=status.HTTP_200_OK)
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)



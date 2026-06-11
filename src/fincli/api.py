"""FastAPI delivery layer -- REST API for fincli."""

import json
import os
import urllib.request

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from supabase import create_client

load_dotenv()

app = FastAPI(title="fincli API", version="1.0.0")

_API_URL = "https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL"


def _get_client():
    url = os.environ["SUPABASE_URL"]
    key = os.environ["SUPABASE_KEY"]
    return create_client(url, key)


def _fetch_rates() -> dict | None:
    try:
        with urllib.request.urlopen(_API_URL, timeout=5) as response:
            return json.loads(response.read())
    except Exception:
        return None


class ExpenseIn(BaseModel):
    description: str
    amount: float


@app.get("/")
def root():
    return {"message": "fincli API is running"}


@app.post("/expenses", status_code=201)
def add_expense(expense: ExpenseIn):
    if not expense.description.strip():
        raise HTTPException(status_code=422, detail="Description cannot be empty.")
    if expense.amount <= 0:
        raise HTTPException(status_code=422, detail="Amount must be positive.")
    client = _get_client()
    response = client.table("expenses").insert({
        "description": expense.description.strip(),
        "amount": expense.amount,
    }).execute()
    return response.data[0]


@app.get("/expenses")
def list_expenses():
    client = _get_client()
    response = client.table("expenses").select("*").order("id").execute()
    return response.data


@app.delete("/expenses/{expense_id}", status_code=204)
def remove_expense(expense_id: int):
    client = _get_client()
    response = client.table("expenses").delete().eq("id", expense_id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Expense not found.")


@app.get("/total")
def get_total():
    client = _get_client()
    response = client.table("expenses").select("amount").execute()
    total = sum(row["amount"] for row in response.data)
    result = {"total_brl": round(total, 2)}
    rates = _fetch_rates()
    if rates:
        usd = rates.get("USDBRL", {})
        eur = rates.get("EURBRL", {})
        btc = rates.get("BTCBRL", {})
        if usd.get("bid"):
            result["total_usd"] = round(total / float(usd["bid"]), 2)
            result["usd_variation"] = usd.get("pctChange")
        if eur.get("bid"):
            result["total_eur"] = round(total / float(eur["bid"]), 2)
            result["eur_variation"] = eur.get("pctChange")
        if btc.get("bid"):
            result["total_btc"] = round(total / float(btc["bid"]), 8)
    return result
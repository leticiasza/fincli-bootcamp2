"""Supabase adapter -- implements ExpenseRepository using PostgreSQL."""

import os

from dotenv import load_dotenv
from supabase import Client, create_client

from fincli.models import Expense, ExpenseBook
from fincli.repository import ExpenseRepository

load_dotenv()


def _get_client() -> Client:
    url = os.environ["SUPABASE_URL"]
    key = os.environ["SUPABASE_KEY"]
    return create_client(url, key)


class SupabaseRepository(ExpenseRepository):
    """Stores expenses in Supabase (PostgreSQL)."""

    def load(self) -> ExpenseBook:
        client = _get_client()
        response = client.table("expenses").select("*").execute()
        expenses = [
            Expense(description=row["description"], amount=row["amount"])
            for row in response.data
        ]
        return ExpenseBook(expenses=expenses)

    def save(self, book: ExpenseBook) -> None:
        pass
        
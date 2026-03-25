"""JSON file adapter — implements the ExpenseRepository port."""

import json
from pathlib import Path

from fincli.models import Expense, ExpenseBook
from fincli.repository import ExpenseRepository

_DEFAULT_PATH = Path.home() / ".fincli" / "expenses.json"


class JsonFileRepository(ExpenseRepository):
    """Stores expenses in a local JSON file."""

    def __init__(self, path: Path = _DEFAULT_PATH) -> None:
        self._path = path

    def load(self) -> ExpenseBook:
        if not self._path.exists():
            return ExpenseBook()
        with self._path.open("r", encoding="utf-8") as f:
            raw: list[dict] = json.load(f)
        return ExpenseBook(
            expenses=[Expense(**item) for item in raw]
        )

    def save(self, book: ExpenseBook) -> None:
        self._path.parent.mkdir(parents=True, exist_ok=True)
        with self._path.open("w", encoding="utf-8") as f:
            json.dump(
                [
                    {"description": e.description, "amount": e.amount}
                    for e in book.expenses
                ],
                f,
                indent=2,
                ensure_ascii=False,
            )

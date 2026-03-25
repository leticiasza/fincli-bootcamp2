"""Application service — orchestrates use-cases without touching I/O."""

from dataclasses import dataclass

from fincli.models import Expense
from fincli.repository import ExpenseRepository


@dataclass
class ExpenseDTO:
    index: int
    description: str
    amount: float


class FinanceService:
    """
    Pure use-case orchestrator.
    Receives a repository via constructor injection (Dependency Inversion).
    Contains zero print/input calls — those belong to the CLI layer.
    """

    def __init__(self, repo: ExpenseRepository) -> None:
        self._repo = repo

    # ------------------------------------------------------------------ #
    # Use-cases                                                            #
    # ------------------------------------------------------------------ #

    def add_expense(self, description: str, amount: float) -> Expense:
        """UC-01 — Validate and persist a new expense."""
        expense = Expense(description=description, amount=amount)
        book = self._repo.load()
        book.add(expense)
        self._repo.save(book)
        return expense

    def list_expenses(self) -> list[ExpenseDTO]:
        """UC-02 — Return all expenses as DTOs."""
        book = self._repo.load()
        return [
            ExpenseDTO(index=i, description=e.description, amount=e.amount)
            for i, e in enumerate(book.expenses)
        ]

    def remove_expense(self, index: int) -> Expense:
        """UC-03 — Remove expense by index and persist."""
        book = self._repo.load()
        removed = book.remove(index)
        self._repo.save(book)
        return removed

    def get_total(self) -> float:
        """UC-04 — Return the sum of all expense amounts."""
        book = self._repo.load()
        return book.total()

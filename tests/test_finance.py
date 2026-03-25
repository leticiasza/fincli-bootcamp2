"""Automated tests — all domain & service logic, zero I/O."""

import pytest

from fincli.models import Expense, ExpenseBook
from fincli.repository import ExpenseRepository
from fincli.services import FinanceService

# ------------------------------------------------------------------ #
# In-memory test double (stub)                                         #
# ------------------------------------------------------------------ #


class InMemoryRepository(ExpenseRepository):
    """Fake repository — holds data in memory, never touches disk."""

    def __init__(self) -> None:
        self._book = ExpenseBook()

    def load(self) -> ExpenseBook:
        return self._book

    def save(self, book: ExpenseBook) -> None:
        self._book = book


# ------------------------------------------------------------------ #
# Fixtures                                                             #
# ------------------------------------------------------------------ #


@pytest.fixture()
def service() -> FinanceService:
    return FinanceService(repo=InMemoryRepository())


# ------------------------------------------------------------------ #
# Test — UC-01: add expense                                            #
# ------------------------------------------------------------------ #


def test_add_expense_persists_correctly(service: FinanceService) -> None:
    """A valid expense must be stored and retrievable."""
    service.add_expense("Coffee", 5.50)
    expenses = service.list_expenses()

    assert len(expenses) == 1
    assert expenses[0].description == "Coffee"
    assert expenses[0].amount == pytest.approx(5.50)


def test_add_multiple_expenses(service: FinanceService) -> None:
    """Adding several expenses must preserve insertion order."""
    service.add_expense("Lunch", 32.00)
    service.add_expense("Bus", 4.50)
    expenses = service.list_expenses()

    assert len(expenses) == 2
    assert expenses[0].description == "Lunch"
    assert expenses[1].description == "Bus"


# ------------------------------------------------------------------ #
# Test — UC-01 validation: invalid amount                              #
# ------------------------------------------------------------------ #


def test_add_expense_rejects_negative_amount(service: FinanceService) -> None:
    """Negative amounts must raise ValueError."""
    with pytest.raises(ValueError, match="positive"):
        service.add_expense("Refund", -10.00)


def test_add_expense_rejects_zero_amount(service: FinanceService) -> None:
    """Zero amounts must raise ValueError."""
    with pytest.raises(ValueError, match="positive"):
        service.add_expense("Free item", 0)


def test_add_expense_rejects_empty_description(service: FinanceService) -> None:
    """Blank descriptions must raise ValueError."""
    with pytest.raises(ValueError, match="empty"):
        service.add_expense("   ", 10.00)


# ------------------------------------------------------------------ #
# Test — UC-04: total calculation                                      #
# ------------------------------------------------------------------ #


def test_total_is_sum_of_all_amounts(service: FinanceService) -> None:
    """Total must equal the arithmetic sum of all expense amounts."""
    service.add_expense("Rent", 1200.00)
    service.add_expense("Groceries", 350.75)
    service.add_expense("Internet", 99.90)

    assert service.get_total() == pytest.approx(1650.65)


def test_total_is_zero_when_no_expenses(service: FinanceService) -> None:
    """Total must be 0.0 when the book is empty."""
    assert service.get_total() == pytest.approx(0.0)


# ------------------------------------------------------------------ #
# Test — UC-03: remove expense                                         #
# ------------------------------------------------------------------ #


def test_remove_expense_by_valid_index(service: FinanceService) -> None:
    """Removing by a valid index must reduce the list."""
    service.add_expense("Gym", 89.90)
    service.add_expense("Streaming", 39.90)

    removed = service.remove_expense(0)

    assert removed.description == "Gym"
    assert len(service.list_expenses()) == 1
    assert service.list_expenses()[0].description == "Streaming"


def test_remove_expense_invalid_index_raises(service: FinanceService) -> None:
    """Removing with an out-of-range index must raise IndexError."""
    service.add_expense("Gym", 89.90)

    with pytest.raises(IndexError):
        service.remove_expense(99)


# ------------------------------------------------------------------ #
# Test — Domain model unit tests                                       #
# ------------------------------------------------------------------ #


def test_expense_book_is_empty_initially() -> None:
    book = ExpenseBook()
    assert book.is_empty()
    assert book.total() == 0.0


def test_expense_book_total_updates_after_add() -> None:
    book = ExpenseBook()
    book.add(Expense("A", 10.0))
    book.add(Expense("B", 20.0))
    assert book.total() == pytest.approx(30.0)

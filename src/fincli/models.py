"""Domain models — pure data, zero I/O."""

from dataclasses import dataclass, field


@dataclass
class Expense:
    """A single financial expense."""

    description: str
    amount: float

    def __post_init__(self) -> None:
        if not self.description or not self.description.strip():
            raise ValueError("Description cannot be empty.")
        if self.amount <= 0:
            raise ValueError(f"Amount must be positive, got {self.amount}.")
        self.description = self.description.strip()


@dataclass
class ExpenseBook:
    """Aggregate root — an ordered collection of expenses."""

    expenses: list[Expense] = field(default_factory=list)

    def add(self, expense: Expense) -> None:
        self.expenses.append(expense)

    def remove(self, index: int) -> Expense:
        if index < 0 or index >= len(self.expenses):
            raise IndexError(
                f"Index {index} out of range (0–{len(self.expenses) - 1})."
            )
        return self.expenses.pop(index)

    def total(self) -> float:
        return sum(e.amount for e in self.expenses)

    def is_empty(self) -> bool:
        return len(self.expenses) == 0

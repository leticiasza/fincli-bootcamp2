"""Repository port — abstract persistence contract."""

from abc import ABC, abstractmethod

import fincli.models


class ExpenseRepository(ABC):
    """Port that any storage adapter must implement."""

    @abstractmethod
    def load(self) -> fincli.models.ExpenseBook:
        """Load and return the full expense book."""

    @abstractmethod
    def save(self, book: fincli.models.ExpenseBook) -> None:
        """Persist the full expense book."""

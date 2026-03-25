"""CLI layer — presentation only, delegates everything to FinanceService."""

import sys

from fincli.adapters import JsonFileRepository
from fincli.services import FinanceService

_SEPARATOR = "─" * 44


def _build_service() -> FinanceService:
    """Compose the dependency graph (poor-man's DI container)."""
    return FinanceService(repo=JsonFileRepository())


def _fmt_amount(value: float) -> str:
    return f"R$ {value:,.2f}"


# ------------------------------------------------------------------ #
# Commands                                                             #
# ------------------------------------------------------------------ #


def cmd_add(service: FinanceService, args: list[str]) -> None:
    if len(args) < 2:
        print("Usage: fincli add <description> <amount>")
        sys.exit(1)
    description = " ".join(args[:-1])
    try:
        amount = float(args[-1].replace(",", "."))
    except ValueError:
        print(f"[erro] '{args[-1]}' is not a valid number.")
        sys.exit(1)

    try:
        expense = service.add_expense(description, amount)
    except ValueError as exc:
        print(f"[erro] {exc}")
        sys.exit(1)

    print(f"✔  Added: {expense.description} — {_fmt_amount(expense.amount)}")


def cmd_list(service: FinanceService) -> None:
    expenses = service.list_expenses()
    if not expenses:
        print("No expenses recorded yet.")
        return
    print(_SEPARATOR)
    print(f"{'#':<4} {'Description':<28} {'Amount':>10}")
    print(_SEPARATOR)
    for dto in expenses:
        print(f"{dto.index:<4} {dto.description:<28} {_fmt_amount(dto.amount):>10}")
    print(_SEPARATOR)
    print(f"{'Total':<33} {_fmt_amount(service.get_total()):>10}")
    print(_SEPARATOR)


def cmd_remove(service: FinanceService, args: list[str]) -> None:
    if len(args) < 1:
        print("Usage: fincli remove <index>")
        sys.exit(1)
    try:
        index = int(args[0])
    except ValueError:
        print(f"[erro] '{args[0]}' is not a valid index.")
        sys.exit(1)

    try:
        removed = service.remove_expense(index)
    except IndexError as exc:
        print(f"[erro] {exc}")
        sys.exit(1)

    print(f"✔  Removed: {removed.description} — {_fmt_amount(removed.amount)}")


def cmd_total(service: FinanceService) -> None:
    total = service.get_total()
    print(f"Total spent: {_fmt_amount(total)}")


# ------------------------------------------------------------------ #
# Entry-point                                                          #
# ------------------------------------------------------------------ #

HELP = """
fincli — Personal Finance CLI  v1.0.0

Commands:
  add <description> <amount>   Add a new expense
  list                         List all expenses
  remove <index>               Remove expense by index
  total                        Show total spent
  help                         Show this help message
"""


def main() -> None:
    args = sys.argv[1:]
    if not args or args[0] in ("help", "--help", "-h"):
        print(HELP)
        return

    service = _build_service()
    command = args[0]
    rest = args[1:]

    match command:
        case "add":
            cmd_add(service, rest)
        case "list":
            cmd_list(service)
        case "remove":
            cmd_remove(service, rest)
        case "total":
            cmd_total(service)
        case _:
            print(f"[erro] Unknown command '{command}'. Run 'fincli help'.")
            sys.exit(1)

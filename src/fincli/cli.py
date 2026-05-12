"""CLI layer — presentation only, delegates everything to FinanceService."""

import json
import sys
import urllib.request

from fincli.adapters import JsonFileRepository
from fincli.services import FinanceService

_SEPARATOR = "─" * 44
_API_URL = "https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL"


def _build_service() -> FinanceService:
    """Compose the dependency graph (poor-man's DI container)."""
    return FinanceService(repo=JsonFileRepository())


def _fmt_amount(value: float) -> str:
    return f"R$ {value:,.2f}"


def _fetch_rates() -> dict | None:
    """Busca cotações na AwesomeAPI. Retorna None se falhar."""
    try:
        with urllib.request.urlopen(_API_URL, timeout=5) as response:
            return json.loads(response.read())
    except Exception:
        return None


def _fmt_variation(pct: str) -> str:
    value = float(pct)
    arrow = "+" if value >= 0 else ""
    return f"{arrow}{value:.2f}%"


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

    print(f"Adicionado: {expense.description} — {_fmt_amount(expense.amount)}")


def cmd_list(service: FinanceService) -> None:
    expenses = service.list_expenses()
    if not expenses:
        print("Nenhum gasto registrado ainda.")
        return
    print(_SEPARATOR)
    print(f"{'#':<4} {'Descricao':<28} {'Valor':>10}")
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
        print(f"[erro] '{args[0]}' nao e um indice valido.")
        sys.exit(1)

    try:
        removed = service.remove_expense(index)
    except IndexError as exc:
        print(f"[erro] {exc}")
        sys.exit(1)

    print(f"Removido: {removed.description} — {_fmt_amount(removed.amount)}")


def cmd_total(service: FinanceService) -> None:
    total = service.get_total()

    print(_SEPARATOR)
    print(f"  Total gasto: {_fmt_amount(total)}")
    print(_SEPARATOR)

    rates = _fetch_rates()
    if rates is None:
        print("  Cotacao indisponivel no momento.")
        print(_SEPARATOR)
        return

    usd = rates.get("USDBRL", {})
    eur = rates.get("EURBRL", {})
    btc = rates.get("BTCBRL", {})

    if usd.get("bid"):
        usd_val = total / float(usd["bid"])
        var_usd = _fmt_variation(usd.get("pctChange", "0"))
        print(f"  USD: $ {usd_val:,.2f}   (dolar {var_usd} hoje)")

    if eur.get("bid"):
        eur_val = total / float(eur["bid"])
        var_eur = _fmt_variation(eur.get("pctChange", "0"))
        print(f"  EUR: € {eur_val:,.2f}   (euro  {var_eur} hoje)")

    if btc.get("bid"):
        btc_val = total / float(btc["bid"])
        print(f"  BTC: ₿ {btc_val:.8f}")

    print(_SEPARATOR)


# ------------------------------------------------------------------ #
# Entry-point                                                          #
# ------------------------------------------------------------------ #

HELP = """
fincli — Controle de Financas Pessoais  v1.0.0

Comandos:
  add <descricao> <valor>   Adicionar um gasto
  list                      Listar todos os gastos
  remove <indice>           Remover gasto pelo indice
  total                     Ver total gasto com cotacao em tempo real
  help                      Exibir esta mensagem
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
            print(f"[erro] Comando '{command}' desconhecido. Execute 'fincli help'.")
            sys.exit(1)

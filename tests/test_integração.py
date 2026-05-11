"""Teste de integracao com a AwesomeAPI."""

from fincli.cli import _fetch_rates


def test_api_retorna_bid_usd():
    """Valida que a API retornou cotacao do dolar com campo bid preenchido."""
    rates = _fetch_rates()
    assert rates is not None, "API nao respondeu"
    assert "USDBRL" in rates, "Campo USDBRL ausente"
    assert rates["USDBRL"].get("bid"), "Campo bid do dolar veio vazio"


def test_api_retorna_bid_eur():
    """Valida que a API retornou cotacao do euro com campo bid preenchido."""
    rates = _fetch_rates()
    assert rates is not None, "API nao respondeu"
    assert "EURBRL" in rates, "Campo EURBRL ausente"
    assert rates["EURBRL"].get("bid"), "Campo bid do euro veio vazio"


def test_api_retorna_bid_btc():
    """Valida que a API retornou cotacao do bitcoin com campo bid preenchido."""
    rates = _fetch_rates()
    assert rates is not None, "API nao respondeu"
    assert "BTCBRL" in rates, "Campo BTCBRL ausente"
    assert rates["BTCBRL"].get("bid"), "Campo bid do bitcoin veio vazio"
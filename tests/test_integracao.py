"""Teste de integracao com a AwesomeAPI."""

import json
from unittest.mock import patch

from fincli.cli import _fetch_rates

MOCK_RESPONSE = {
    "USDBRL": {"bid": "5.20", "pctChange": "-0.66"},
    "EURBRL": {"bid": "5.80", "pctChange": "-0.12"},
    "BTCBRL": {"bid": "350000.00", "pctChange": "1.20"},
}


def test_api_retorna_bid_usd():
    with patch("fincli.cli.urllib.request.urlopen") as mock:
        mock.return_value.__enter__ = lambda s: s
        mock.return_value.__exit__ = lambda s, *a: False
        mock.return_value.read.return_value = json.dumps(MOCK_RESPONSE).encode()
        rates = _fetch_rates()
    assert rates is not None, "API nao respondeu"
    assert "USDBRL" in rates
    assert rates["USDBRL"].get("bid"), "Campo bid do dolar veio vazio"


def test_api_retorna_bid_eur():
    with patch("fincli.cli.urllib.request.urlopen") as mock:
        mock.return_value.__enter__ = lambda s: s
        mock.return_value.__exit__ = lambda s, *a: False
        mock.return_value.read.return_value = json.dumps(MOCK_RESPONSE).encode()
        rates = _fetch_rates()
    assert rates is not None, "API nao respondeu"
    assert "EURBRL" in rates
    assert rates["EURBRL"].get("bid"), "Campo bid do euro veio vazio"


def test_api_retorna_bid_btc():
    with patch("fincli.cli.urllib.request.urlopen") as mock:
        mock.return_value.__enter__ = lambda s: s
        mock.return_value.__exit__ = lambda s, *a: False
        mock.return_value.read.return_value = json.dumps(MOCK_RESPONSE).encode()
        rates = _fetch_rates()
    assert rates is not None, "API nao respondeu"
    assert "BTCBRL" in rates
    assert rates["BTCBRL"].get("bid"), "Campo bid do bitcoin veio vazio"

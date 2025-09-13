# pytest .\test_convert.py -v --no-header
# ^^^ test command

from helpers import currency
import helpers.env as env
import pytest

def test_valid_convert():
    assert currency.convert(env.get("API_KEY"), ['1', 'usd', 'cad']) == "Current rate: 1 USD = 1.38545 CAD"
    assert currency.convert(env.get("API_KEY"), ['1', 'XCD', 'cad']) == "Current rate: 1 XCD = 0.512645 CAD"
    assert currency.convert(env.get("API_KEY"), ['1', 'usd', 'JPY']) == "Current rate: 1 USD = 147.6685 JPY"


def test_invalid_convert():
    with pytest.raises(ValueError):
        assert currency.convert(env.get("API_KEY"), "cat")
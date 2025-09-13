# pytest .\test_convert.py --tb=no -v --no-header
# ^^^ test command

from helpers import currency
import helpers.env as env
import pytest

def test_valid_convert():
    assert currency.convert(env.get("API_KEY"), ['1', 'usd', 'cad']) == "1 USD = 1.38545 CAD"
    assert currency.convert(env.get("API_KEY"), ['1', 'XCD', 'cad']) == "1 XCD = 0.512645 CAD"
    assert currency.convert(env.get("API_KEY"), ['1', 'usd', 'JPY']) == "1 USD = 147.6685 JPY"


def test_invalid_convert():
    with pytest.raises(ValueError):
        assert currency.convert(env.get("API_KEY"), "cat")
        
    with pytest.raises(TypeError):
        assert currency.convert(env.get("API_KEY"), 231423)

    assert currency.convert(env.get("API_KEY"), "1 usd to cad") == "Failed to convert! :("
    assert currency.convert(env.get("API_KEY"), "1 sdf sfdo sdf") == "Failed to convert! :("

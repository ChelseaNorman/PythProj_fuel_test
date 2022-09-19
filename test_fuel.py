from fuel import convert, gauge
import pytest

def test_convert():
        assert convert("1/4") == 25
        assert convert("1/2") == 50
        assert convert("1/5") == 20
        with pytest.raises(ZeroDivisionError):
                convert("1/0")
        with pytest.raises(ValueError):
                convert("4/3")

def test_gauge():
        assert gauge(1) == "E"
        assert gauge(25) == "25%"
        assert gauge(99) == "F"

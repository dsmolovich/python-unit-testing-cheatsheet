# SRC: https://docs.pytest.org/en/7.1.x/how-to/parametrize.html#parametrize-basics

import pytest

@pytest.mark.parametrize("a, b, expected", [
    (1,1,2), (-1,-1,-2), (0,0,0), (0,1,1), (5_000_000, 3_000_000, 8_000_000)])
def test_sum(a, b, expected):
    assert a+b == expected


@pytest.mark.parametrize("n, expected",[
    (1,2), (2,3), (5_000_000, 5_000_001), (-1,0)])
class TestClass:
    def test_simple_case(self, n, expected):
        assert n+1 == expected
    
    def test_weird_case(self, n, expected):
        assert (n*1) + 1 == expected


@pytest.mark.parametrize("n, expected",[
    (1,2), pytest.param(2,4, marks=pytest.mark.xfail)])
def test_simple_case(n, expected):
    assert n+1 == expected


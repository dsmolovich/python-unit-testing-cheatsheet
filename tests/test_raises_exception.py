import pytest

class SomeClass:
    def some_method(self):
        raise Exception("exception message")


def test_raises_exception():
    sut = SomeClass()
    with pytest.raises(Exception) as exc_info:
        sut.some_method()
        assert exc_info.value == "exception message"

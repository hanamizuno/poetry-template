"""Test Hello world"""
from src.hello import hello


def test_hello_01() -> None:
    assert hello() == "Hello, world!"


def test_hello_02() -> None:
    assert hello("Python") == "Hello, Python!"

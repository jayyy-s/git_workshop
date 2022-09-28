from main import foo
from main import bar


def test_foo():
    assert foo(3) == 3


def test_bar():
    assert bar(3) == 6

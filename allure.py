import pytest

def test_foo():
    pytest.allure.attach('my attach', 'Hello, World')
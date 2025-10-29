import pytest
from app import hello_world, add_numbers


def test_hello_world():
    """Test 2 the hello_world function."""
    assert hello_world() == "Hello, World!"


def test_add_numbers():
    """Test the add_numbers function."""
    assert add_numbers(2, 3) == 5
    assert add_numbers(0, 0) == 0
    assert add_numbers(-1, 1) == 0
    assert add_numbers(10, -5) == 5


def test_add_numbers_with_floats():
    """Test add_numbers with float inputs."""
    assert add_numbers(1.5, 2.5) == 4.0
    assert add_numbers(0.1, 0.2) == pytest.approx(0.3)

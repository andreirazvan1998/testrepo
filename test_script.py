import os
import pytest

from simple_script import write_message,add_numbers

from simple_script import write_message,add_numbers,multiply_numbers,subtract_numbers


def test_write_message():
    write_message()
    assert os.path.exists("output.txt")

def test_add_numbers():
    assert add_numbers(2, 3) == 6
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0

def test_multiply_numbers():
    assert multiply_numbers(2, 3) == 6
    assert multiply_numbers(-1, 5) == -5
    assert multiply_numbers(0, 10) == 0
    assert multiply_numbers(4, 4) == 16

def test_subtract_numbers():
    assert subtract_numbers(10, 4) == 6
    assert subtract_numbers(5, 5) == 0
    assert subtract_numbers(0, 7) == -7
    assert subtract_numbers(-3, -7) == 4

if __name__ == "__main__":
    pytest.main()
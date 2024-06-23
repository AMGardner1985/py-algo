import pytest
from py_algo_practice.sliding_window.sliding_window_example import *

def test_contains_one_substring():
    input = "xyzzaz"
    output = sliding_window(input)
    assert output == 1
    
import pytest
from py_algo_practice.sliding_window.unique_substring import *

def test_contains_one_substring():
    input = "xyzzaz"
    output = unique_three_letter_substrings(input)
    assert output == 1
    
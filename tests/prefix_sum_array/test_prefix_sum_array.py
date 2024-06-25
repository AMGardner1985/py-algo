from typing import List
from py_algo_practice.prefix_sum.prefix_sum import prefix_sum_array_example
import pytest



def test_prefix_sum_array():
    input = [1,2,3,4,5]
    expected = [1,3,6,10,15]
    assert prefix_sum_array_example(input) == expected
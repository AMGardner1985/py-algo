import pytest
from py_algo_practice.two_pointer import remove_duplicate_sorted


def test_removeDuplicatesAndReturnNumberOfUniqueElements():
    input = [1,1,2]
    expectedOutput = 2
    results = remove_duplicate_sorted.removeDuplicates(input)
    assert results == expectedOutput
    
    
    
    
    
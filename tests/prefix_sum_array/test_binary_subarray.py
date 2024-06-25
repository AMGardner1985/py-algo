
from typing import List
import pytest

def test_num_subarray_with_sum():
    input = [1,0,1,0,1]
    goal = 2
    expected_output = 4
    assert num_subarray_with_sum(input, goal) == expected_output
    
    
def num_subarray_with_sum(input : List[int], goal : int) -> int:
    total_count = 0
    current_sum = 0
    
    frequency = {}
    
    for num in input:
        current_sum += num
        if current_sum == goal:
            total_count += 1
        
        # check if there is any prefix sum that can be subtracted from current sum to get desired goal
        if (current_sum - goal) in frequency:
            total_count += frequency[current_sum - goal]
            
        # populate dictionary with current sum plus 1 
        # useful patter for one line populate dictionary
        frequency[current_sum] = frequency.get(current_sum,0) + 1
        
    return total_count
        
            
        
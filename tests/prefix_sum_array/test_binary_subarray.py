
from typing import List
import pytest

'''
given you have an array with 1's and 0's and a target/goal integer (e.g. 2)

return the number of subarrays where the sum of those ones and zeros equals my goal


basically this is a combo of a sliding window question and a prefix sum question 

'''


def test_num_subarray_with_sum():
    input = [1,0,1,0,1]
    goal = 2
    expected_output = 4
    assert num_subarray_with_sum(input, goal) == expected_output



def subarray_sum(nums : List[int], k: int) -> int:
    res = 0
    curSum = 0
    prefixSums = { 0 : 1 }
    
    for n in nums:
        curSum += n
        diff = curSum - k
        res += prefixSums.get(diff, 0)
        prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)
            
    
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
        
            
###
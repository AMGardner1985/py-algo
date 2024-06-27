'''
This algorithim uses the construction of a dictionary while going through a data object
to help calculate possible subarrays that fit some criteria such as (matching a sum / having a range / continous / etc..)
this can be used in combination of prefix sum array

it is just a tricky way of subsectioning an array based on what has been seen so far
'''

from collections import defaultdict

def find_subarray_fit_criteria(test_array, k):
    counts = defaultdict(int)
    counts[0] = 1
    
    answer = 0
    current = 0
    
    for numbers in test_array:
        # do logic to change current
        answer += counts[current - k]
        counts[current] += 1
    
    return answer
    
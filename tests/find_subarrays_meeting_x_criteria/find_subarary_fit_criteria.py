'''
This algorithim uses the construction of a dictionary while going through a data object
to help calculate possible subarrays that fit some criteria such as (matching a sum / having a range / continous / etc..)
this can be used in combination of prefix sum array

it is just a tricky way of subsectioning an array based on what has been seen so far
'''

from collections import defaultdict

def find_subarray_fit_criteria(test_array, goal):
    # create a dictionary to hold only what has been see so far (don't pre-poulate this)
    counts = defaultdict(int)
    counts[0] = 1
    
    answer = 0
    current = 0
    
    for numbers in test_array:
        # do logic to change current
        
        # the answer is the count of items that meet the criteria - the goal
        needed_scenario_or_number = current - goal
        
        #checks what has been seen if there is the needed umber or scenario in it, if so 
        # #get the count of how many times that has happend and add it to the running count/ answer
        answer += counts[needed_scenario_or_number]
        
        counts[current] += 1
    
    return answer
    
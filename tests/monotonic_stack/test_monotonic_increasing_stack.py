
'''
This algorithim uses a stack to help track what the next greater (or lower) or equal item could be.  
There is an example when you need to transform an array to be what the next greatest number would be 

'''
from typing import List
import pytest

def monotonic_increasing_stack(arr):
    stack = []
    answer = 0
    
    
    for num in arr:
        # for monotonic decreasinc just flip the > to < 
        
        # while the stack has a value in it AND the value in the stake compared to the current number doesn't 
        # meets criteria (ex it is bigger than current number)
        while stack and stack[-1] > num: 
            # do logic
            
            # remove the last item while the item is greater than current number
            stack.pop()
           
        stack.append(num)
        
    return answer



'''
given an array (its circular uggghhh...) return the next greater number for every element
if can't find greater number then return -1
# '''
# def test_next_greater_element():
#     input = nums = [1,2,3,4,3]
#     expected_output = [2,3,4,-1,4]
#     results = get_next_larger_element_in_circular_array(input)
#     assert results == expected_output
    


def test_next_greater_element_I():
    # https://leetcode.com/problems/next-greater-element-i/description/
    nums1 = [4,1,2]
    nums2 = [1,3,4,2]
    expected_output = [-1,3,-1]
    
    results = next_greater_element(nums1, nums2)
    assert results == expected_output
    
    
def next_greater_element(nums1 : List[int], nums2: List[int]) -> List[int]:
    
    # create a dictionary of number and index of nums1
    index_dictionary = { n: i for i,n in enumerate(nums1)}
    
    #create results array with all values defaulted to -1 (not found)
    result = [-1] * len(nums1)
    
    #create empty stack to hold values in increasing order
    stack = []
    
    for i in range(len(nums2)):
        #current number to evaluate
        current_value = nums2[i]
        
        while stack and current_value > stack[-1]:
            # if the current number is greater than last value in the stack
            value = stack.pop()
            
            # get index of last item on stack from the input array
            value_index = index_dictionary[value]
            
            #set the number in the results array to the last value found in the stack
            result[value_index] = current_value
        
        if current_value in index_dictionary:
            stack.append(current_value)
    
    return result
            
            
        
        
def test_final_prices():
    prices = [10,1,1,6]
    expected = [9,0,1,6]
    assert finalPrices(prices) == expected
    
def finalPrices(prices: List[int]) -> List[int]:
    stack = []
    for i in range(len(prices)):
        while stack and (prices[stack[-1]] >= prices[i]):
            prices[stack.pop()] -= prices[i]
        stack.append(i)

    return prices

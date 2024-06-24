
from typing import List


def test_key_greater_than_zero():
    input_array = [5,7,1,4]
    key = 3
    expected_results = [12,10,16,13]
    assert decrypt(input_array, key) == expected_results
    
def test_key_less_than_zero():
    input_array = [2,4,9,3]
    key = -2
    expected_results = [12,5,6,13]
    assert decrypt(input_array, key) == expected_results
    

def test_zero_code():
    input_array = [5,7,1,4]
    key = 0
    expected_results = [0,0,0,0]
    assert decrypt(input_array, key) == expected_results
    
    
'''
your are given a numberical array and a a key number to create a defuse code.
you need to repace all the numbers in the array at one time. 
you need to transform the array by 3 different criteria
    - if key > 0 then the target number is changed to the sum of next k numbers
    - if key < 0 then replace target number with the sum of the previous k numbers
    - if the key is 0 replace the target number with 0
'''    
def decrypt(code : List[int], key: int) -> List[int]:
    
        if key == 0:
            return __decode_key_is_zero(code)
        
        if key > 0:
            return __decode_key_greater_than_zero(code, key)
        
        if key < 0:
            return __decode_key_less_than_zero(code, key)
        
        
def __decode_key_is_zero(code : List[int]) -> List[int]:
    output = []
    left = 0
    
    while left < len(code):
        output.append(0)
        left += 1

    return output


def __decode_key_greater_than_zero(code : List[int], key : int) -> List[int]:
    output = []
    left = 0
    running_sum = 0
    
    while left < len(code):
        if left > 0:
            running_sum -= code[left]
            
            calculated_pointer = left + key
            if calculated_pointer >= len(code):
                    calculated_pointer = calculated_pointer - len(code) 
        
            running_sum += code[calculated_pointer]
            
            
        if left == 0:
            for i in range(key):
                calculated_pointer = left + (i + 1)
                
                # circle around to start of array again if needed
                if calculated_pointer >= len(code):
                    calculated_pointer = calculated_pointer - len(code) 
        
                running_sum += code[calculated_pointer]
        
            
        output.append(running_sum)
        left += 1

    return output


def __decode_key_less_than_zero(code : List[int], key: int):
    output = []
    left = 0
    while left < len(code):
        # get all of the items for the key number of elements before left
        running_sum = 0
        absolute_key = abs(key)
        for i in range (absolute_key):
            calculated_pointer = left - (i + 1)
            if calculated_pointer < 0:
                calculated_pointer = (len(code)) - abs(calculated_pointer)
            running_sum += code[calculated_pointer]
        left += 1
        output.append(running_sum)
    return output
            
        
'''
[longest harmonious subsequence] (https://leetcode.com/problems/longest-harmonious-subsequence/description/)

given an array of int
return a subsequence of the integers so that the range from highest to lowest int in subsequence is 1,  
you can remove numbers from the array
you can't resort the array 
return the count of the subsequnce. 


a harmonious array is difference between max value and min value is only 1
-subsequence can be any numbers in the array
    - you can remove numbers
    - you can NOT sort the numbers

input = 1,3,2,2,5,2,3,7
output = 5 
explanation (3,2,2,2,3)


what did i learn?  I got focused on the non sorting of the array and that took me away from a more simple solution.  collections.counter is also awesome in python
'''


import collections


def test_for_five_ubsequence_found():
    input = [1,3,2,2,2,5,3,7]
    expected_output = 5
    assert get_harmonious_subsequence_non_sliding_window(input) == expected_output
    

def test_no_subsequence_found():
    input = [1,1,1,1,1,1,1,1]
    expected_output = 0 
    assert get_harmonious_subsequence_non_sliding_window(input) == expected_output
    
def test_small_sequence_should_return_two():
    input = [1,2,3,4]
    expected_output = 2 
    assert get_harmonious_subsequence_non_sliding_window(input) == expected_output


def get_harmonious_subsequence_non_sliding_window(test_array) -> int:
    count = collections.Counter(test_array)
    answer = 0
    for x in count:
        if x + 1 in count:
            answer = max(answer, (count[x] + count[x + 1]))
    return answer
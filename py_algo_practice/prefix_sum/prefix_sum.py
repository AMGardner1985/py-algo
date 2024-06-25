'''
prefix sum

-- this is just a light version of dynamic programming
-- you are calculating something and storing it, then using those storred calculations for future use
array = [1,2,3,4,5]
prefix sum array = [1,3,6,10,15]

you calculate prefix_sum_array[0], then use prefix_sum_array[0] + array[1] to calculate prefix_sum_array[1]. 

This is a common way to optimize a calculation 

There are some tricky calculations you can do like getting the sum of psa[1] + psa[n] by taking psa[n+1] - psa[0]

'''

from typing import List


def prefix_sum_array_example(input_array : List[int]) -> List[int]:
    # starts array with first number
    prefix = [input_array[0]]
    for i in range(1, len(input_array)):
        prefix.append(prefix[-1] + input_array[i])
    
    return prefix


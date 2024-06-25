'''
given a string, return the length of the largest substring where it contains at most two occurences of each letter. 

-- so retrun length of substring that has a max of two occuences of each letter
-- substream has all the letters
-- substring has no more than 2 of any letter


--contain no more than 2 letters for any letter?

'''

def test_setup():
    input = "bcbbbcba"
    expected_output = 4
    results = get_max_length_of_substring_with_two_occurrences(input)
    assert results == expected_output
    
    
    
    
    
def get_max_length_of_substring_with_two_occurrences(input_string : str) -> int:
    left_pointer = 0
    right_pointer = 0
    map = {}
    max_length = 0
    
    while right_pointer < len(input_string):
        # update map
        if input_string[right_pointer] not in map:
            map[input_string[right_pointer]] = 1
        else:
            map[input_string[right_pointer]] += 1 
            
        # check criteria
        while map[input_string[right_pointer]] > 2:
            map[input_string[left_pointer]] -= 1
            if map[input_string[left_pointer]] == 0:
                del map[input_string[left_pointer]]
            left_pointer += 1
        
        max_length = max(max_length, (right_pointer - left_pointer + 1))
        right_pointer += 1
        
    return max_length
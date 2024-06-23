

def sliding_window(test_string : str) -> int:
    answer = 0
    left = 0
    right = 2
    
    print(len(test_string))
    
    # loop to move the sliding window through data object
    while right < len(test_string):   
        # if condition to check goes here
        if (test_string[left] != test_string[left + 1] and
            test_string[left] != test_string[right] and
            test_string[left + 1] != test_string[right]): 
            
            answer += 1
            left += 1
            right += 1
        else: 
            left += 1
            right += 1
    
    return answer
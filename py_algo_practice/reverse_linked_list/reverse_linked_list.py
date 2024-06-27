
def reverse_linked_list(head): 
    current = head
    previous = None
    while current:
        next_node = current.next 
        previous = current 
        current = next_node
    
    return previous
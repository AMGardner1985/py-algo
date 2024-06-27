
import pytest

from py_algo_practice.list_node import ListNode


def test_algo():
    simple_linked_list =  ListNode(1)
    
    for index in range(6):
        current_node = simple_linked_list
        current_node.next = ListNode(index)
        current_node = current_node.next
    
    
    reversed_list = reverse_linked_list(simple_linked_list)
    
    
    assert reversed_list.val == 5 
    
    
def reverse_linked_list(head: ListNode) -> ListNode:
    current = head
    previous = None
    
    while current:
        temp_node_to_process_next = current.next
        
        current.next = previous
        previous = current
        
        current = temp_node_to_process_next
    
    return previous
        

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
def detectCycle(node: ListNode) -> bool:
    
    
    slow = node
    fast = node.next
    
    if slow == None or fast == None:
        return False
    
    # continue while both nodes are not null
    while slow and fast: 
        # if both nodes are equal then there is a cycle at some point
        if slow == fast:
            return False
        
        slow = slow.next
        fast = fast.next.next
    
    # will only be reached if one of the noes is null thus there is no cycle
    return True
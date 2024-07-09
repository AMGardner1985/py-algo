from collections import deque
from typing import Optional
import pytest

from py_algo_practice.tree_node import TreeNode

def test_setup():
    root = TreeNode(2,TreeNode(1),TreeNode(3))
    expected = TreeNode(2,TreeNode(3),TreeNode(1))
    results = invert_tree(root)
    
    assert results.left.val == 3
    assert results.right.val == 1
    

def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is None:
        return root     
    
    queue = deque()
    queue.append(root)
    
    while queue:
        items_in_level = len(queue)
        
        for _ in range(items_in_level):
            node = queue.popleft()
            
            temp_node = node.left
            node.left = node.right
            node.right = temp_node
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
    
    return root
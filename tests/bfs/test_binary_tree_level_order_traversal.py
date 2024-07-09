
from collections import deque

from typing import List, Optional

from py_algo_practice.tree_node import TreeNode

'''
given root of binary tree, return level order traversal of its nodes values from left to right and level by level


ex

input = 
     3
     /\
    9   20
        / \
       15  7
       
output =  [[3], [9,02] [15,7]]

'''


def test_should_return_empty_array():
    root = None
    expected = []
    assert expected == level_order(root)

def test_should_return_single_node():
    root = TreeNode(1)
    expected = [[1]]
    assert expected == level_order(root)
    
def test_should_return_multiple_levels():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    expected = [[3], [9,20]]
    assert expected == level_order(root)
    
    
    
    
    
def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    if root is None:
        return []
    
    queue = collections.deque()
    queue.append(root)
    answer = []
    
    while queue:
        
        current_level_length = len(queue)
        current_level_value = []

        for _ in range(current_level_length):
            node = queue.popleft()    
            
            current_level_value.append(node.val)         
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        answer.append(current_level_value)
        
    return answer
    
'''
given an integer array with no duplicates

a max binary tree can be built recursively from nums using an algorithim
- create node whose value is the max value in nums
- left is everything left 

'''

from typing import List, Optional
import pytest


class TreeNode:
    def __init__(self, val=0, left=None, right=None)
        self.val = val
        self.left = left
        self.right = right

def test_example_one():
    input_nums = [3,2,1,6,0,5]
    expected_output =  [6,3,5,None,2,0,None,None,1]
    
    

def construct_max_binary_tree(nums: List[int]) -> Optional[TreeNode]:
    nodes = []
    
    for num in nums:
        node = TreeNode(num)
        
        while nodes and num > nodes[-1].val:
            node.left = nodes.pop()
        
        # no stack item is < current number
        # nodes_stack.append(node)
    
    return TreeNode()

import pytest
from py_algo_practice.graph_node import GraphNode
from py_algo_practice.tree_node import * 


root = TreeNode(0)

def dfs_pattern(root: TreeNode):
        # exit clause
        if not root:
            return
        
        ans = 0
        
        # do logic (example could number of nodes that have a value of "this one")
        if root.val == "this one":
            ans += 1
        
        
        # traverse down the left all the way
        ans += dfs_pattern(root.left)
        
        # once done all the lefts will include the rights as well down that path
        ans += dfs_pattern(root.right)
        
        return ans 
        
    
def dfs_pattern_iteractive(root: TreeNode):
    stack = [root]
    ans = 0
    while stack:
        node = stack.pop()
        # do logic to process current node
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return ans
    
def dfs_pattern_for_graph_with_possible_cycle(graph):
    
    def dfs_graph(node):
        answer = 0
        #do some logic
        for neighbor in graph[graph]:
            if neighbor not in seen: 
                seen.add(neighbor)
                answer += dfs(neighbor)
        return answer 
                
    seen = {graph}
    return dfs_graph(graph)
        
        


from collections import deque


def bfs(root):
    queue = deque([root])
    answer = 0
    
    while queue:
        current_length = len(queue)
        
        #do logic at current level of graph
        
        #index isn't used could possible use something like while queue as well
        for index in range(current_length):
            
            #this popleft is because we want first in first out to ensure doing current level before moving on
            node = queue.popleft() 
            # do logic needed
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
    return answer
            
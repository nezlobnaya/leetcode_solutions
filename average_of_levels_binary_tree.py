from collections import defaultdict
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        sumOfNodes = defaultdict(float)
        levels = defaultdict(int)
       
        def dfs(node, l):
            if not node: return
            dfs(node.left, l+1)
            dfs(node.right, l+1)
            sumOfNodes[l] += node.val
            levels[l] +=1
            
        dfs(root,0)
              
        return [sumOfNodes[i]/levels[i] for i in range(len(sumOfNodes))]


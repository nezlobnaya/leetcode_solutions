# Definition for a binary tree node.
from typing import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        dic = defaultdict(list)
        
        def dfs(node, level):
            if not node: return
            
            dic[level].append(node.val)
            dfs(node.left, level+1)
            dfs(node.right, level +1)
            
        dfs(root,0)
        
        return dic.values()
            
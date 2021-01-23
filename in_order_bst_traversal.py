# Definition for a binary tree node.
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
#recursive          
        res = []
        def aux(root):
            
            if root:
                aux(root.left)
                res.append(root.val)
                aux(root.right)
     
        aux(root)
        return res
      
#interative
        # if not root:
        #     return
        # stack = []
        # res,current = deque(), root
        # while current or res:
        #     if current:
        #         res.append(current)
        #         current = current.left
        #     else:
        #         current = res.pop()
        #         stack.append(current.val)
        #         current = current.right
        # return stack
        
"""
230. Kth Smallest Element in a BST

with iterative in order traversal(dfs)
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if root is None: return 
        stack = []
        counter = 0
        
        while True:
            if root is not None:
                stack.append(root)
                root = root.left

            else:
                if stack is None: break
                root = stack.pop()
                counter  +=1 
                if counter== k: return root.val
                root = root.right
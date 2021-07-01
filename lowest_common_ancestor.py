# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans= None
        
        def dfs(node):
            if not node: return False
            left = dfs(node.left)
            right = dfs(node.right)
            current=node ==p or node ==q
            if (left and right) or (current and right) or (current and left):
                self.ans = node
                return
            return left or right or current
        dfs(root)
        return self.ans

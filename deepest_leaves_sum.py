# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        def max_depth(node,depth):
            if node is None: return (0,-1)       
            
            if node.left is None and node.right is None:
                return(node.val, depth)
            
            left = max_depth(node.left,depth + 1)
            right = max_depth(node.right,depth + 1)
        
            if left[1] == right[1]:
                return (left[0] +right[0], left[1])
            elif left[1] > right[1]:
                return left
            else: return right

        return max_depth(root,0)[0]
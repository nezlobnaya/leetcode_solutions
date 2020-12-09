# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        
        if root is None: return 0

        asset = self.recurse_find_maxDiff(root)

        return asset['diff']

    def recurse_find_maxDiff(self, root: TreeNode) -> dict:
      # assets
        max_diff = 0
        vals = []
        
        if root.left is not None:
            diff_asset_left = self.recurse_find_maxDiff(root.left)
# asset batching on left side of tree
            if diff_asset_left['diff'] > max_diff: max_diff = diff_asset_left['diff']
            vals += diff_asset_left['vals']
              
        if root.right is not None:
            diff_asset_right = self.recurse_find_maxDiff(root.right)
# asset batching on right side of tree
            if diff_asset_right['diff'] > max_diff: max_diff = diff_asset_right['diff']
            vals += diff_asset_right['vals']

        for i in vals:
            max_diff = max(
                abs(root.val - i), max_diff
            )
            
        vals += [root.val]

        return {
            'diff': max_diff,
            'vals': vals
        }
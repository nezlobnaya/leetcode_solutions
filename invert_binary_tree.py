# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
      return str(self.val)


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        if root:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root

        
def traverse(root):
    current_level = [root]
    while current_level:
        print(' '.join(str(node) for node in current_level))
        next_level = list()
        for n in current_level:
            if n.left:
                next_level.append(n.left)
            if n.right:
                next_level.append(n.right)
        current_level = next_level


root  = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.right = TreeNode(9)
root.right.left = TreeNode(6)
print("Input Tree")
traverse(root)

print("Reversed Tree")

Solution().invertTree(root)
traverse(root)
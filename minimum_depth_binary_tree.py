"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


#a queue of tuples(node.val,depth)
#bfs

from queue import Queue
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = Queue()
        queue.put((root, 1))
        while True:
            node, depth  = queue.get()
            if not node.left and not node.right:
                return depth
            if node.right:
                queue.put((node.right, depth +1))
            if node.left:
                queue.put((node.left, depth +1))
            

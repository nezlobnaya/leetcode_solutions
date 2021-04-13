# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
            # empty tree has height 0
        if root is None:
            return 0
 
    # create an empty queue and enqueue root node
        queue = deque()
        queue.append(root)
 
        height = 0
 
    # loop till queue is empty
        while queue:
 
        # calculate number of nodes in current level
            size = len(queue)
 
        # process each node of current level and enqueue their
        # non-empty left and right child to queue
            while size > 0:
                front = queue.popleft()
 
                if front.left:
                    queue.append(front.left)
 
                if front.right:
                    queue.append(front.right)
 
                size = size - 1
 
        # increment height by 1 for each level
            height = height + 1
 
        return height
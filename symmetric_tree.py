# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # recursive
#         def is_Mirror(node1, node2):
#             if node1 is None and node2 is None: return True
#             if node1 is None or node2 is None: return False
#             return (node1.val == node2.val) and is_Mirror(node1.right, node2.left) and is_Mirror(node1.left, node2.right)
#         return is_Mirror(root, root)
    # iterative
        queue = deque()
        queue.append(root)
        queue.append(root)
        while queue:
            t1=queue.popleft()
            t2=queue.popleft()
            if t1 is None and t2 is None: continue
            if t1 is None or t2 is None: return False
            if t1.val != t2.val: return False
            queue.append(t1.left)
            queue.append(t2.right)
            queue.append(t1.right)
            queue.append(t2.left)
        return True
            
        
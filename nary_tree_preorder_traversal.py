class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:return
        q =deque([root])
        output = []
        while q:
            candidate = q.popleft()
            output.append(candidate.val)
            for child in reversed(candidate.children):
                q.appendleft(child)
        return output
                
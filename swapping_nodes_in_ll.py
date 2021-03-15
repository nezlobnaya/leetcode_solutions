"""
1721. Swapping Nodes in a Linked List

"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        if head is None: return None
        current = head
        ans = []
        while current:
            ans.append(current)
            current = current.next
        ans[k-1].val, ans[len(ans)-k].val = ans[len(ans)-k].val, ans[k-1].val
        
        return head
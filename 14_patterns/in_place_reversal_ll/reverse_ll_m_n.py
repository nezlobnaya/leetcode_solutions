"""
Reverse a linked list from position m to n. Do it in one-pass.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or m == n: return head
        dummy = ListNode(0)
        dummy.next = head
        current = head
        prev = dummy
        
        for _ in range(m-1):     
            current = current.next
            prev = prev.next
            
        
        for _ in range(n-m):
            current.next.next, prev.next, current.next = prev.next, current.next, current.next.next

        return dummy.next
    
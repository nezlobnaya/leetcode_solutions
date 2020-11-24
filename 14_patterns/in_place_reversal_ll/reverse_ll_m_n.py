"""
Reverse a linked list from position m to n. Do it in one-pass.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return str(self.val) + "->" + str(self.next)
class Solution:
    def reverseBetween(self, head, m, n):
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

if __name__ == "__main__":
    l1 = ListNode(0,1)
    l2 = ListNode(1,2)
    l3 = ListNode(2,3)
    l4 = ListNode(3,4)
    l5 = ListNode(4,5)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    
    print((f"Linked List: {l1}"))
    print((f"Reversed LL: {Solution().reverseBetween(l1,2,4)}"))
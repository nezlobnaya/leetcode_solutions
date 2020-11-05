"""
fast slow pointers
"""
def isPalindrome(self, head):
     def reverse(head):
            prev=None
            while head:
                temp=head.next
                head.next=prev
                prev=head
                head=temp
            return prev
		
        if head is None: return True
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        one=head
        two=reverse(slow)
        while one and two:
            if one.val!=two.val:
                return False
            one=one.next
            two=two.next
        return True










# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        node = head
        stack = []
        while node:
            stack.append(node.val)
            node = node.next
        node = head
        for i in stack[::-1]:
            if (i != node.val):
                return False
            node = node.next
        return True
                
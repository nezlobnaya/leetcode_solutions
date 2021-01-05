"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Solution

We can solve this question by using a set.

We traverse the linked list and check if the next node’s value is inside the set.

If it is, then we modify the current node’s next value to cur.next.next ( delete the next node).

Otherwise, we add cur.next’s value to the set and continue traversing the linked list.

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return str(self.val) + "->" + str(self.next)    
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        items = set()
        items.add(head.val)
        cur = head

        while cur and cur.next:
            if cur.next.val in items:
                cur.next = cur.next.next
            else:
                items.add(cur.next.val)
                cur = cur.next
    
        return head

def main():
  head = ListNode(1)
  head.next = ListNode(2)
  head.next.next = ListNode(3)
  head.next.next.next = ListNode(2)
  head.next.next.next.next = ListNode(5)
  head.next.next.next.next.next = ListNode(5)
  head.next.next.next.next.next.next = ListNode(5)

  print(f"Test case one:  {head}")

  print(f"Duplicates deleted: {Solution().deleteDuplicates(head)}")



main()
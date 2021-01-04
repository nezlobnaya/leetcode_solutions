"""
Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        while (fast is not None and fast.next is not None):
            slow = slow.next
            fast = fast.next.next
        return slow

def main():
  head = ListNode(1)
  head.next = ListNode(2)
  head.next.next = ListNode(3)
  head.next.next.next = ListNode(4)
  head.next.next.next.next = ListNode(5)

  print("Middle Node: " + str(Solution().middleNode(head).val))

  head.next.next.next.next.next = ListNode(6)
  print("Middle Node: " + str(Solution().middleNode(head).val))

  head.next.next.next.next.next.next = ListNode(7)
  print("Middle Node: " + str(Solution().middleNode(head).val))


main()
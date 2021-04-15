class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy1 = current1 = ListNode(0)
        dummy2 = current2 = ListNode(0)

        while head:
            if head.val < x:
                current1.next = head
                current1 = current1.next
            else:
                current2.next = head
                current2 = current2.next
            head = head.next
        current2.next =None
        current1.next = dummy2.next

        return dummy1.next
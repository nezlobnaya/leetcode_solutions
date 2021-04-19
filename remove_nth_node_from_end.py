# two passes solution works
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:  
        dummy = ListNode(0, next=head)
        current= head
        length = 0

        while current:
            current = current.next
            length +=1
        if length == 1: return None
        current = dummy
        for _ in range(length-n):             
            current = current.next
        current.next = current.next.next
        return dummy.next

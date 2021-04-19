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

# one pass solution added:   
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:  
        dummy = fast = slow= ListNode(0, next=head)
        for _ in range(n):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next
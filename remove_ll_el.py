# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return str(self.val) + "->" + str(self.next)    

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        prev, current = dummy, head
        while current:
            if current.val == val:
                prev.next = current.next
            else:
                prev = current
            current = current.next
        return dummy.next 

def main():
  head = ListNode(1)
  head.next = ListNode(2)
  head.next.next = ListNode(6)
  head.next.next.next = ListNode(3)
  head.next.next.next.next = ListNode(4)
  head.next.next.next.next.next = ListNode(5)
  head.next.next.next.next.next.next = ListNode(6)

  print(f"LL to test:  {head}")
  val = 6
  print(f"Nodes with value {val} deleted: {Solution().removeElements(head,val)}")

main()
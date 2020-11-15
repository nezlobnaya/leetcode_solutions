# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
      return str(self.val) + "->" + str(self.next)
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry_over = 0
        p = newLL = ListNode(0)
        while l1 or l2 or carry_over:
            if l1:
                carry_over += l1.val
                l1 = l1.next
            if l2:
                carry_over += l2.val
                l2 = l2.next
            p.next = ListNode(carry_over%10)
            carry_over //= 10
            p = p.next
        return (f"Result: {newLL.next}")

l1_1 = ListNode(2)
l1_2 = ListNode(4)
l1_3 = ListNode(3)

l1_1.next = l1_2
l1_2.next = l1_3

print((f"List1: {l1_1}"))


l2_1 = ListNode(5)
l2_2 = ListNode(6)
l2_3 = ListNode(4)

l2_1.next = l2_2
l2_2.next = l2_3

print((f"List2: {l2_1}"))


s = Solution()

print(s.addTwoNumbers(l1_1,l2_1))



# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.       
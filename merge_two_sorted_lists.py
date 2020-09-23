# Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

# Example:

# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        current = merged_list = ListNode()
        
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        if l1:
            current.next = l1
        if l2:
            current.next = l2
            
        return merged_list.next
# new_s = Solution()

# l1 = l2 = ListNode()
# l1 = [1,2,4]
# l2 = [1,3,4]

# print(f"Merged Sorted Array: {new_s.mergeTwoLists(l1, l2)}")

# # if __name__ == '__main__':
# #     # Use the main function here to test out the implementation
# #     l1 = [1,2,4]
# #     l2 = [1,3,4]

# #     print(f"Merged Sorted Array: {mergeTwoLists(l1, l2)}")
# #     # Output: 1->1->2->3->4->4
    
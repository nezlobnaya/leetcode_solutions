"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

"""
from typing import List 
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def combineLists(self, l1, l2):
        newList = ListNode(None)
        cur = newList
    
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
    
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
    
        return newList.next

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        else:
            i, j = 0, 1
            newLists = []
            while j < len(lists):
                l1, l2 = lists[i], lists[j]
                combined = self.combineLists(l1, l2)
                newLists.append(combined)
                i += 2
                j += 2
            if len(lists) & 1:
                newLists.append(lists[-1])
            
            return self.mergeKLists(newLists)
        

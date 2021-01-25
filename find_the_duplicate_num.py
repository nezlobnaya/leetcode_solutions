from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        ptr1 = nums[0]
        while ptr1 != hare:
            ptr1 = nums[ptr1]
            hare = nums[hare]
        return ptr1
        
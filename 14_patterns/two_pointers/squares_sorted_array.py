"""
Given an array of integers A sorted in non-decreasing order,
 return an array of the squares of each number, 
also in sorted non-decreasing order.

"""


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted([x*x for x in A])

# Two pointers

class Solution:
    def sortedSquares(self, arr: List[int]) -> List[int]:
        start, end, result = 0, len(arr)-1, list()
        while start < end:
            if arr[start]**2 > arr[end]**2:
                result.append(arr[start]**2)
                start += 1
            elif arr[start]**2 == arr[end]**2:
                result.append(arr[start]**2)
                result.append(arr[end]**2)
                start += 1
                end -= 1
            elif arr[start]**2 < arr[end]**2:
                result.append(arr[end]**2)
                end -= 1
        if start == end:
            result.append(arr[start]**2)
        return result[::-1]
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hash = {}
        # for i in range(len(nums)):
        #     element = target - nums[i]
        #     if element in hash:
        #         return hash[element], i
        #     else:
        #         hash[nums[i]] = i
        # return None
        hash = {}
        for i,num in enumerate(nums):
            element = target - num
            if element in hash:
                return hash[element], i
            else:
                hash[num] = i
        return None

def main():
    nums=[2,7,11,15]
    target = 9

    print(f'indices of the two numbers such that they add up to {target}: {Solution().twoSum(nums, target)}')

main()
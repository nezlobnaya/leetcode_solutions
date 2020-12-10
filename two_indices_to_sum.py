class Solution:
    def twoSum(self, nums, target):
        hash = {}
        for i in range(len(nums)):
            element = target - nums[i]
            if element in hash:
                return hash[element], i
            else:
                hash[nums[i]] = i
        return None
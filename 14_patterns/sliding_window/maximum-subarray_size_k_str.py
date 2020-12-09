import collections
class Solution:
    def maxSlidingWindow(self, nums, k):

        res = []
        q = collections.deque()
        for i, num in enumerate(nums):
            while q and nums[q[-1]] < num:
                q.pop()
            q.append(i)
            if q[0]<=i-k:
                q.popleft()
            if i>=k-1:
                res.append(nums[q[0]])
        return res
        
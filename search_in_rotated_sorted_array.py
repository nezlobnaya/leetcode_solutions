class Solution:
    def search(self, nums, target):
        left=0 
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target: return True
            if nums[left]==nums[mid]==nums[right]:
                left+=1; right-=1
            elif nums[left]<=nums[mid]:
                if nums[left]<=target<nums[mid]: right=mid-1
                else: left=mid+1
            else:
                if nums[mid]<=target<nums[left]: left=mid+1
                else:right=mid-1
        return False
        
if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2]
    for target in [4,5,6,7,0,1,2,2,10]:
        print(Solution().search(nums, target))
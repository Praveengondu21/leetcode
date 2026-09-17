class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums.sort()
        count=1
        max1=1
        if not nums:
            return 0
        for i in range(len(nums)):
            if nums[i]==nums[i-1]:
                continue
            if nums[i]-nums[i-1]==1:
                count+=1
                if max1<count:
                    max1=count
            else:
                count=1
        return max1
        
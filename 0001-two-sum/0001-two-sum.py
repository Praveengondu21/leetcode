class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            c=target-nums[i]
            if c not in d:
                d[nums[i]]=i
            else:
                return d[c],i
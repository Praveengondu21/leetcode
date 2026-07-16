class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left=0
        s=sum(nums)
        for i in range(len(nums)):
            if(left==s-left-nums[i]):
                return i
            else:
                left+=nums[i]
        return -1        

        
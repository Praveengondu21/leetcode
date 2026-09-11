class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p=[1]*len(nums)
        pre=1
        for i in range(len(nums)):
            p[i]=pre
            pre*=nums[i]
        suf=1
        for i in range(len(nums)-1,-1,-1):
            p[i]=p[i]*suf
            suf*=nums[i]
        return p
        
        
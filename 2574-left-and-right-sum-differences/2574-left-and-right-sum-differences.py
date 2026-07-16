class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        res=[]
        s=sum(nums)
        left=0
        for i in nums:
            x=abs(left-(s-left-i))
            res.append(x)
            left+=i
        return res    
        
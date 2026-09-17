class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        n=set(nums)
        max1=0
        for i in n:
            if i-1 not in n:
                cur=i
                l=1
                while cur+1 in n:
                    l+=1
                    cur+=1
                if l>max1:
                    max1=l
        return max1
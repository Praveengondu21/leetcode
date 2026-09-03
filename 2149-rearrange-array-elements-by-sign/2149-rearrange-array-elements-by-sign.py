class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        f=[]
        s=[]
        r=[]
        for i in nums:
            if i>0:
                f.append(i)
            else:
                s.append(i)
        for i,j in zip(f,s):
            r.append(i)
            r.append(j)
        return r

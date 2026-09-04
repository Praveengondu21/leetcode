class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        f=[]
        s=[]
        for i in nums:
            if i%2==0:
                f.append(i)
            else:
                s.append(i)
        r=[]
        for i,j in zip(f,s):
            r.append(i)
            r.append(j)
        return r
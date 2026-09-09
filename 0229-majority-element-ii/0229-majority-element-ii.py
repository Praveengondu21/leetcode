class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d={}
        l=[]
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for k,v in d.items():
            if v>(len(nums)/3):
                l.append(k)
        return l
        
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i%2==0:
                if i not in d:
                    d[i]=1
                else:
                    d[i]+=1
        if not d:
            return-1
        me=min(d.keys())
        for k,v in d.items():
            if d[k]>d[me]:
                me=k
            if d[k]==d[me] and k<me:
                me=k
        return me
            
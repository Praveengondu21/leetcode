class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        is_found=False
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in d.values():
            if i>1:
                is_found=True
                break
        return is_found

        
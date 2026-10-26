class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashk = {}
        for i in nums:
            if hashk.get(i,0) >=1:
                return True
            hashk[i] = hashk.get(i,0)+1
        return False
        
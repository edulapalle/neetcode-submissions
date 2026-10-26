class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Create a hashset to store numbers
        hset = {}
        #loop through nums list
        for i in nums:
            hset[i] = hset.get(i,0) + 1
        for i in hset.values():
            if i >1:
                return True
        return False
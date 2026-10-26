class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setx = set(nums)
        if len(nums) != len(setx):
            return True
        return False
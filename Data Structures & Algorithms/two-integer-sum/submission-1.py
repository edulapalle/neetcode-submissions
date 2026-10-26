class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #enumerate built in python tool, helps to loop trhough array with adding indices
        prevMap = {} # value, index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap.get(diff),i] #becuse we are checking if data is already present
            prevMap[n] = i

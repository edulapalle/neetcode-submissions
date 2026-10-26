class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for i in strs:
            # create a array for each string
            count = [0]*26
            for x in i:
                #update the count array with alphabet mapping
                count[ ord(x) - ord('a')] += 1
            res[tuple(count)].append(i)
        return list(res.values())
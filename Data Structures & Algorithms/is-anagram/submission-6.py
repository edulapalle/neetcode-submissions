class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #edge case:
        if len(s) != len(t):
            return False
        hashs, hasht = {},{}
        for i in s:
            hashs[i] = hashs.get(i,0) + 1
        for i in t:
            hasht[i] = hasht.get(i,0) + 1
        for i in hashs.keys():
            if hashs.get(i,0) != hasht.get(i,0):
                return False
        return True
            
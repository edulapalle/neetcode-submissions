class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        length = len(s)
        dicts = {}
        dictt = {}
        for i in range(0 , length, 1):
            dicts[s[i]] = dicts.get(s[i],0) + 1
            
        for j in range(0, length, 1):
            dictt[t[j]] = dictt.get(t[j],0) + 1
        
        if dicts == dictt:
            return True
        return False

        
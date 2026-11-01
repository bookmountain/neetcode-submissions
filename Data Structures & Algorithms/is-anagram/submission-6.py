class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False;

        sCounts = {}
        for i in s:
            if i in sCounts:
                sCounts[i] += 1
            else: 
                sCounts[i] = 1
        
        tCounts = {}
        for j in t:
            if j in tCounts:
                tCounts[j] += 1
            else:
                tCounts[j] = 1

        for k in range(len(s)):
            if sCounts.get(s[k], 0) != tCounts.get(s[k],0):
                return False
        return True
        

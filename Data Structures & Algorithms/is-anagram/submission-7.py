class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        m1 = {}
        m2 = {}
        
        for char in s:
            if char in m1:
                m1[char] += 1
            else: m1[char] = 0

        for char in t:
            if char in m2:
                m2[char] += 1
            else: m2[char] = 0

        for char in s:
            if char not in m2 or m1[char] != m2[char]:
                return False
        return True
        

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        m1 = {}
        m2 = {}
        
        for char in s:
            m1[char] = 1 + m1.get(char, 0)

        for char in t:
            m2[char] = 1 + m2.get(char, 0)

        for char in s:
            if char not in m2 or m1[char] != m2[char]:
                return False
        return True
        

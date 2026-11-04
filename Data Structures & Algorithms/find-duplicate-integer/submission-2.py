class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        map = {}
        for i, n in enumerate(nums):
            if n in map:
                return n
            map[n] = i
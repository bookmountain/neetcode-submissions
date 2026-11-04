class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        setnums = set(nums)
        for n in setnums:
            if n - 1 not in setnums:
                start = n
                count = 0
                while start in setnums:
                    start += 1
                    count += 1
                    if count > longest:
                        longest = count
        return longest
                
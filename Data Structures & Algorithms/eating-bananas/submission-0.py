class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lower, upper = 1, max(piles) 
        res = upper
        while lower <= upper:
            mid = (lower + upper) // 2
            hours = sum(math.ceil(p / mid) for p in piles)
            if hours <= h:
                res = mid
                upper = mid - 1
            else:
                lower = mid + 1

        return res

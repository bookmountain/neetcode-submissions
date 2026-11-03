class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0
        for n in nums:
            if n == 0:
                zero_count += 1
            else:
                product = product * n
                
        if zero_count >= 2:
            return [0] * len(nums)

        res = []
        for i, n in enumerate(nums):
            if n == 0:
                res = [0] * len(nums)
                res[i] = product
                
                return res

            else:
                res.append(product // n)

        return res
class Solution:
    def findMin(self, nums: List[int]) -> int:
            n = len(nums) - 1
            l = 0
            r = n

            while l <= r:
                mid = (l+r) // 2
                if l == r:
                    break
                if nums[mid] > nums[r]:
                    l = mid + 1
                else:
                    r = mid
            return nums[r]
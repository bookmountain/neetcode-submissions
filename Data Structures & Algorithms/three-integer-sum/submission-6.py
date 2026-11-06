class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [-4, -1, -1, 0, 1, 2]
        nums.sort()

        res = []
        # -nums[i] = nums[j] + nums[k]
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if -nums[i] == nums[j] + nums[k]:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1 
                elif -nums[i] > nums[j] + nums[k]:
                    j += 1
                else:
                    k -= 1
        
        return res
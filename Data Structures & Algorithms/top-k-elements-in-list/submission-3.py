class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        sorted_descending = dict(sorted(count.items(), key=lambda item: item[1], reverse=True)[:k])
        
        return [key for key, _value in sorted_descending.items()]
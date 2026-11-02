class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        frequents_tuples = counts.most_common(k)

        return [element for element, frequency in frequents_tuples]
        
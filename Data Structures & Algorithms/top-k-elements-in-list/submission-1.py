class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        num_sort = sorted(c, key=c.get, reverse=True)
        print(num_sort)
        return num_sort[:k]

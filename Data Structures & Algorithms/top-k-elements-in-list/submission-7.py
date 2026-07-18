class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for n in nums:
            frequency[n] = frequency.get(n, 0) + 1
        print(frequency)
        return [n for n,_ in sorted(frequency.items(), key= lambda x : x[1], reverse=True)][:k]
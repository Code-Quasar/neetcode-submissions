class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        apperence = dict()
        for n in nums:
            idx = apperence.get(n, -1)
            if idx == -1:
                apperence[n] = 1
            else:
                return True
        return False
        
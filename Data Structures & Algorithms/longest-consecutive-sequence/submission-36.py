class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        nums = [n + abs(nums[0]) - k for k, n in enumerate(nums)]
        if len(nums) < 2: return len(nums)
        
        current_max = 1
        maximum = 1
        print(nums)
        for k,v in enumerate(nums[:-1]):
            if v == nums[k+1]:
                current_max +=1
            else:
                current_max = 1
            maximum = max(maximum, current_max)

        print(nums)
        return maximum

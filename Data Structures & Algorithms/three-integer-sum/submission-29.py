class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums = sorted(nums)
        print(nums)

        for k,n in enumerate(nums):
            l = k+1
            r = len(nums) - 1
            while l < r :
                if n + nums[l] + nums[r] < 0:
                    l += 1
                elif n + nums[l] + nums[r] > 0:
                    r -= 1  
                else:
                    if sorted([n, nums[l], nums[r]]) not in results:
                        results.append(sorted([n, nums[l], nums[r]]))
                    l += 1
                    r -= 1                
        return results
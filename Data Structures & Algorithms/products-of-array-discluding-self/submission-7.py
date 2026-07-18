class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        for i,_ in enumerate(nums) :
            output.append(1)
            for p,q in enumerate(nums):
                if p != i:
                    output[i] *= q
        return output
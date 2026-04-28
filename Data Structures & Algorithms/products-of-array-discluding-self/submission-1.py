class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)

        for i, m in enumerate(nums):
            mup = 1
            for j, n in enumerate(nums):
                if i!=j:
                    mup*=n
            res[i] = mup
        return res
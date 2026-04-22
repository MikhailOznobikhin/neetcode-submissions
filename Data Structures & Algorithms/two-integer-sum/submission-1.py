class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {} # target - n: indx
        
        for indx, n in enumerate(nums):
            if n in d:
                return [d[n], indx]
            d[target-n] = indx

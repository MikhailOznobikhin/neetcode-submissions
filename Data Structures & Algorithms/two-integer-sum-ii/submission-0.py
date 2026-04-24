class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {} # target - num: indx
        for indx, num in enumerate(numbers):
            if num in d:
                return [d[num], indx+1]
            d[target-num]=indx+1
        
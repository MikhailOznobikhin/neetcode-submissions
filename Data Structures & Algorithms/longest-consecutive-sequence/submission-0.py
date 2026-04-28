class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            local_res = 1
            if i-1 not in nums:
                while i+1 in nums:
                    local_res +=1
                    i+=1
                res = max(res, local_res)
        return res
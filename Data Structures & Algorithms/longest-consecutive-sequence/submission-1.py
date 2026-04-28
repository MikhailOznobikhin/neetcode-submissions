class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        set_nums=set(nums)
        for i in set_nums:
            local_res = 1
            if i-1 not in set_nums:
                while i+1 in set_nums:
                    local_res +=1
                    i+=1
                res = max(res, local_res)
        return res
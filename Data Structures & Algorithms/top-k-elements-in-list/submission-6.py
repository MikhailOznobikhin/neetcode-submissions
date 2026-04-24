class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_f = defaultdict(int)
        for n in nums:
            dict_f[n]+=1
        sorted_items = sorted(dict_f.items(), key=lambda x: x[1])
        return [num for num, _ in sorted_items[-k:]]
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_f = defaultdict(int) # number: count_sees
        if len(nums)==k:
            return nums
        for i in nums:
            dict_f[i]+=1
        # dict_f {1:1, 2:2, 3:3}
        count_sees = list(dict_f.values())
        count_sees.sort()
        count_sees.reverse()
        print(count_sees)
        print(dict_f)
        res = []
        j=0
        while j < k:
            elem = count_sees[j]
            for num, sees in dict_f.items():
                if sees == elem and num not in res: 
                    res.append(num)
                    break
            j+=1
        # res [3 2 1]
        return res
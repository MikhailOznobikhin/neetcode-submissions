class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}
        for sym in s:
            if sym not in dict_s:
                dict_s[sym]=1
            else:
                dict_s[sym]+=1
        for sym in t:
            if sym not in dict_t:
                dict_t[sym]=1
            else:
                dict_t[sym]+=1

        return dict_s == dict_t
class Solution:
    def conver_str_to_dict(self, word:str)->dict:
        d = {}
        for symbol in word:
            if symbol not in d:
                d[symbol] = 1
            else:
                d[symbol] +=1
        return d

    def anagram_to_string(self, d:dict)->str:
        boo = list(set(d.keys()))
        boo.sort()
        res = ''
        for b in boo:
            res += f"{b}{d[b]}"
        return res

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # собираем словарь по буквам
        set_anagrams = set()
        for word in strs:
            str_anagram = self.anagram_to_string(self.conver_str_to_dict(word))
            set_anagrams.add(str_anagram)
        # у нас есть список анаграм, проходим по словам и ищем подходящую им анаграмму
        print(set_anagrams)

        if not set_anagrams:
            return [strs]
        res = []
        for i in range(len(set_anagrams)):
            res.append([])

        for word in strs:
            anagram = self.conver_str_to_dict(word)
            str_anagram = self.anagram_to_string(self.conver_str_to_dict(word))
            indx = list(set_anagrams).index(str_anagram)
            res[indx].append(word) 
        return res

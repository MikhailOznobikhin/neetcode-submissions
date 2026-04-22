class Solution:
    def conver_str_to_dict(self, word):
        d = {}
        for symbol in word:
            if symbol not in d:
                d[symbol] = 1
            else:
                d[symbol] +=1
        return d

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # собираем словарь по буквам
        set_anagrams = list()

        for word in strs:
            set_anagrams.append(self.conver_str_to_dict(word))
        # у нас есть список анаграм, проходим по словам и ищем подходящую им анаграмму
        res = []
        list_anagrams = []
        for i in range(len(set_anagrams)):
            for j in set_anagrams:
                if set_anagrams[i] != j and j not in list_anagrams:
                    list_anagrams.append(j)
        if not list_anagrams:
            return [strs]
        for i in range(len(list_anagrams)):
            res.append([])

        for word in strs:
            anagram = self.conver_str_to_dict(word)
            for indx, a in enumerate(list_anagrams):
                if a == anagram:
                   res[indx].append(word) 
        return res
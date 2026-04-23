class Solution: # через сортировку
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for word in strs:
            count = [0] * 26 #создаём массив по количеству букв
            for sym in word:
                count[ord(sym)-ord("a")]+=1
            result[tuple(count)].append(word)
        return list(result.values())
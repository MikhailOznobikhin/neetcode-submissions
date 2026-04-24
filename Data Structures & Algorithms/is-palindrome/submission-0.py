class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub("[^a-z0-9]", "", s.lower())
        i=0
        while i < len(s):
            if s[i] != s[len(s)-1-i]:
                return False
            i+=1
        return True
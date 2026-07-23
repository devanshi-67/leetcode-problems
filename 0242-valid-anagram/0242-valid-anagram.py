class Solution:
    def isAnagram(self, s: str, t: str):

        if(s == t):
            return True
        else:
            return sorted(s) == sorted(t)
        
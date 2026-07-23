class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        position = haystack.find(needle)

        if position != -1:
            return position
        else:
            return -1
        
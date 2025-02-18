class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1

        else:
            first = 0

            for i in range(len(haystack)):
                if haystack[i:i+len(needle)] == needle:
                    first = i
                    break
            return first
        
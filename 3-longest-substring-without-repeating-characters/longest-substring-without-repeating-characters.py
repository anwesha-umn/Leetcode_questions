class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        count = 0 
        chars = {}

        for r in range(len(s)):
            if s[r] in chars:
                l = max(l, chars[s[r]] + 1)

            chars[s[r]] = r

            count = max(count, r - l + 1)

        return count
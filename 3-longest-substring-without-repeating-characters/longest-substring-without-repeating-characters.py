class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        chars = {}
        count = 0

        for r in range(len(s)):
            if s[r] in chars:
                l = max(l, chars[s[r]] + 1)
            chars[s[r]] = r  # store characters and indices

            # store max size in count
            count = max(count, r - l + 1)

        return count
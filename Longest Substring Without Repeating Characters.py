# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # initialize dictionary for unique characters
        chars = {}

        l = 0   # left index
        max_length = 0

        for r in range(len(s)):
            
            if s[r] in chars:
                l = max(l,chars[s[r]] + 1) 
                # for repeating char, update left indexx is used to make sure l moves only forward, 
                # not backbard in index
            

            max_length = max(max_length, r-l+1)
            chars[s[r]] = r       # storing characters and latest indices  

        return max_length

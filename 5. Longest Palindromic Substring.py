# 5. Longest Palindromic Substring

# Given a string s, return the longest 
# palindromic substring in s.

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 
class Solution:
    def longestPalindrome(self, s: str) -> str:


        def check(i, j):
            left = i
            right = j-1
            while(left < right):
                if s[left]!=s[right]:
                    return False
                left+=1
                right-=1
            
            return True

        
        for length in range(len(s), 0, -1): # Start from longest substring
            for start in range(len(s)-length+1): # keep updating the start point of substrings
                
                if check(start,start+length):
                    return s[start: start+length]
        
        return ""
        

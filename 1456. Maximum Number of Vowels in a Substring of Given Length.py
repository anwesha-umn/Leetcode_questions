"""
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.


Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.

Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
"""

class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        left = 0
        total = 0
        max_vowels = 0

        # first find total vowels upto k
        for i in range(k):
            if s[i] in "aeiou":
                total += 1
        
        max_vowels = total

        # use sliding window to add/ subtract a vowel
        for right in range(k,len(s)):

            if s[right] in "aeiou":
                total += 1
            if s[left] in "aeiou":
                total -= 1
            
            left += 1
        
            max_vowels = max(max_vowels, total)
            
        return max_vowels

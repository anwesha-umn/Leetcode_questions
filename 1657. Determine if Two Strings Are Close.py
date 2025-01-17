"""
Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.


Example 1:

Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"

Example 2:

Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.

Example 3:

Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"
"""


class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """

        if len(word1) != len(word2):
            return False
        else:
            occur1 = {}
            occur2 = {}

            for i in range(len(word1)):
                if word1[i] not in occur1:
                    occur1[word1[i]] = 1
                else:
                    occur1[word1[i]] += 1

                if word2[i] not in occur2:
                    occur2[word2[i]] = 1
                else:
                    occur2[word2[i]] += 1

            keys1 = sorted([key for key in occur1.keys()])
            keys2 = sorted([key for key in occur2.keys()])

            vals1 = sorted([val for val in occur1.values()])
            vals2 = sorted([val for val in occur2.values()])

            if keys1 == keys2 and vals1 == vals2:
                return True
            else:
                return False

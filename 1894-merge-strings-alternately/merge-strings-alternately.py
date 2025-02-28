class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        chars1 = [char for char in word1]

        chars2 = [char for char in word2]

        merged = []

        while chars1 and chars2:
            merged.append(chars1.pop(0))
            merged.append(chars2.pop(0))

        while chars1:
            merged.append(chars1.pop(0))

        while chars2:
            merged.append(chars2.pop(0))

        return "".join(merged)

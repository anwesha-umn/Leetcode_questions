class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
       

        l = 0
        new = ""
        for r in range(len(t)):

            if l < len(s) and t[r] == s[l]:
                new += s[l]
                l += 1

        if new!=s:
            return False
        else:
            return True

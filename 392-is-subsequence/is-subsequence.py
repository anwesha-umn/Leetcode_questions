class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s=="":
            return True

        l = 0
        new = ""
        for r in range(len(t)):
            if l < len(s) and t[r] == s[l]:
                l += 1
                new += t[r]
            
        
        if new != s:
            return False
        else:
            return True
                

class Solution:
    def reverseWords(self, s: str) -> str:
        
        
        s = s.strip()
        l = s.split()
        l = l[::-1]

        rev = ""
        for s in l:
            rev += s + " "

        return rev.strip()

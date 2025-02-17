class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        i = len(s)-1
        while i>0:
            if s[i]==" ":
                break
            i-=1

        if i > 0:
            return len(s[i+1:])
        else:
            return len(s)
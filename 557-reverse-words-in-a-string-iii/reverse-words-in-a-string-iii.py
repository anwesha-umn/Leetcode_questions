class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        words = s.split(" ")
        new = ""
        
        for word in words:
            word = word[::-1]
            new += word+" "

        return new.strip()
        
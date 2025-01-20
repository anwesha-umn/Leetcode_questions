class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """

        left = 0
        right = 0
        count = 0
        s = ""
        while right < len(chars):

            # if chars[left] not in s:
            #     s += chars[left]
            # else:
            #     right = left + 1

            while right < len(chars) and chars[left] == chars[right]:
                count += 1
                right += 1
            
            if count!=1:
                s += chars[left]+str(count)
            else:
                s += chars[left]
            count=0
            left = right
            
            
        
        for i in range(len(s)):
            chars[i] = s[i]
        chars = chars[:len(s)]
     
        return len(chars)

                

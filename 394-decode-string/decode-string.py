class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        num = 0
        temp = ""
        res = []

        for char in s:
            if char.isdigit():
                num = num*10 + int(char)

            elif char == "[":
                res.append((temp, num))
                temp = ""
                num = 0
            
            elif char == "]":
                string, nums = res.pop()
                temp = string + temp*nums
            else:
                temp += char

        return temp
                
                
                    

                


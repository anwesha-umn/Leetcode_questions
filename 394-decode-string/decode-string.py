class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        num = 0
        stack = [] # LIFO
        num = 0
        temp = ""

        for char in s:

            if char.isdigit():
                num = num * 10 + int(char)

            elif char == "[":
                stack.append((temp, num))
                temp = ""
                num = 0

            elif char == "]":
                string, nums = stack.pop()
                temp = string + temp * nums

            else:
                temp += char

            # print(stack)

        return temp
                
                    

                


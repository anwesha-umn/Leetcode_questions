class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = [] #LIFO
    
        for bracket in s:
            if bracket in "{[(":
                stack.append(bracket)
            else:  
                # for closing bracket "}])" check if last bracket of stack is of same type        
                # check if stack is not empty     
                if not stack or (bracket==")" and stack[-1]!="(") or (bracket=="}" and stack[-1]!="{") or (bracket=="]" and stack[-1]!="["): 
                    return False
                else:
                    stack.pop() 
        size = len(stack)
        if size!=0:
            return False
        else:
            return True
        #return not stack  # if stack is not empty returns False, if stack is empty, returns True

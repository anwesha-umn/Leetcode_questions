# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2**31, 2**31 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21
 

# Constraints:

# -2**31 <= x <= 2**31 - 1

class Solution:
    def reverse(self, x: int) -> int:

        n = abs(x)
        s = 0
        d = 0
        while(n!=0):
            d = n % 10
            s = s*10 + d
            n = n // 10

        if x<0:
            s = s*(-1)

        if s >=-2**31 and s <= 2**31 - 1:
            return s
        else:
            return 0


        

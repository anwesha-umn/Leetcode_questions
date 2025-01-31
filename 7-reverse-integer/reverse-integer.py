class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return x

        num = abs(x)
        if x > 0:
            sign = 1
        else:
            sign = -1
        
        d = 0
        s = 0

        while( num> 0):
            d = num % 10
            s = s*10 + d
            num = num // 10

        res = s * sign
        if res > 2**31-1 or res < -2**31:
            return 0
        else:
            return res

        
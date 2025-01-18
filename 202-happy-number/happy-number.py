class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        def sum_sq(n):
            s = 0
            while n!=0:
                d = n%10
                s = s + d**2
                n = n//10
            return s

        set_n = set()
        # return false if n repeats itself
        while n not in set_n:
            set_n.add(n)
            n = sum_sq(n)
            if n==1:
                return True

        return False

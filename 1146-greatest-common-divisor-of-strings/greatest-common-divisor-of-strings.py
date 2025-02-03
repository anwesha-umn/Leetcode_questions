class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        def gcd(a,b):
            while b!=0:
                a, b = b, a % b
            return a

        str3 = ""
        gcd_len = gcd(len(str1), len(str2))

        str3 = str1[:gcd_len]

        if str3*int(len(str1) // gcd_len) == str1 and str3*int(len(str2) // gcd_len) == str2:
            return str3
        else:
            return ""
        
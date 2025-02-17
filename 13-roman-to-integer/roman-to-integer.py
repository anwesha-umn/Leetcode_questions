class Solution:
    def romanToInt(self, s: str) -> int:

        maps = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        
        value = 0
        i = 0
        for i in range(1,len(s)):
            if maps[s[i]] > maps[s[i-1]]:
                value -= maps[s[i-1]]
            else:
                value += maps[s[i-1]]

        value += maps[s[i]]
        return value

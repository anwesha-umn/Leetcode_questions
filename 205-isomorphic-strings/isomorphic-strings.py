class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        # two dictionary of mappings 
        # map s to t
        s_t = {}

        # map t to s
        t_s = {}

        for i in range(len(s)):
            if s[i] not in s_t:
                s_t[s[i]] = t[i]

            else:
                if s_t[s[i]] != t[i]:
                    return False

            if t[i] not in t_s:
                t_s[t[i]] = s[i]
            else:
                if t_s[t[i]]!=s[i]:
                    return False

        return True
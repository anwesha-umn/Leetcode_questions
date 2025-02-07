class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        map_s_t = {}
        map_t_s = {}

        for i in range(len(s)):
            if s[i] not in map_s_t:
                map_s_t[s[i]] = t[i]
            else:
                if map_s_t[s[i]] != t[i]:  # if already mapped val of map_s_t != current t[i] 
                    return False

            if t[i] not in map_t_s:
                map_t_s[t[i]] = s[i]
            else:
                if map_t_s[t[i]] != s[i]:  # if already mapped val of map_t_s != current s[i] 
                    return False

        return True
        
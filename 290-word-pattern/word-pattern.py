class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        p_s = {}
        s_p = {}

        s_words = s.split()

        if len(s_words)!=len(pattern):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in p_s:
                p_s[pattern[i]] = s_words[i]
            else:
                if p_s[pattern[i]] != s_words[i]:
                    return False

            if s_words[i] not in s_p:
                s_p[s_words[i]] = pattern[i]
            else:
                if s_p[s_words[i]] != pattern[i]:
                    return False

        return True
        
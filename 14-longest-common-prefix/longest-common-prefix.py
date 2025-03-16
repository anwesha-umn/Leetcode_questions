class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        first = strs[0]
        common = 100000000

        for i in range(1,len(strs)):
            curr = strs[i]

            k = 0
            while k < len(curr) and k < len(first) and curr[k] == first[k]:
                k += 1
            common = min(common,k)

        return first[:common]

            

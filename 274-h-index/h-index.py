class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # if len(citations) == 1:
        #     if citations[0]>=1:
        #         return 1
        #     else:
        #         return 0

        max_cite = 0
        for i in range(len(citations)):
            val = citations[i]

            h_index = [1 if cite>=val else 0 for cite in citations]
            # print(h_index)
            
            count = sum(h_index)
            #if count >= val :#and val>0:
            max_cite = max(min(count,val),max_cite)

        return max_cite

        
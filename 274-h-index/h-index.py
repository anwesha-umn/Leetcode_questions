class Solution:
    def hIndex(self, citations: List[int]) -> int:

        max_cite = 0

        for i in range(len(citations)):
            val = citations[i]

            h_index = [cite>=val for cite in citations]
            
            count = sum(h_index)
            
            max_cite = max(min(count,val),max_cite)

        return max_cite

        
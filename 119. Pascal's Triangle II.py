"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]
"""

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        pascal = [[1], [1,1]]
        if rowIndex == 0:
            return pascal[0]

        elif rowIndex == 1:
            return pascal[1]

        else:

            for i in range(2, rowIndex+1):
                l = []
                last = pascal[i-1]

                for j in range(len(last)-1):

                    s = last[j] + last[j+1]
                    l.append(s)

                pascal.append([1]+l+[1])

            return pascal[rowIndex]

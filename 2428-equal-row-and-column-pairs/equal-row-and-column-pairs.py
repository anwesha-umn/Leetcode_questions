class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        pair = 0
        column = []

        for i in range(len(grid)):

            col = []
            for j in range(len(grid)):
                col.append(grid[j][i])
            column.append(col)

            
        for row in grid:
            for col in column:
                if row == col:
                    pair += 1

        return pair


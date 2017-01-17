class Solution(object):
    
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
            """
        n_rows, n_cols = len(grid), len(grid[0])
        for i in range(n_rows):
            for j in range(n_cols):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    grid[i][j] += grid[i][j-1]
                if j == 0:
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
                print 'this step lands at {},{}, with a value of {}'.format(i, j, grid[i][j])

        return grid[n_rows-1][n_cols -1]

s = Solution()
t = s.minPathSum([[1,3,1],[1,5,1],[4,2,1]])

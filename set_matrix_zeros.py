class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n_rows = len(matrix)
        n_cols = len(matrix[0])
        zero_indexs = set()
        for i in range(n_rows):
            zero_pos = [c for c in range(n_cols) if matrix[i][c] == 0]
            zero_indexs = zero_indexs.union(zero_pos)
            if zero_pos:
                matrix[i] = [0] * n_cols
        print zero_indexs
        for i in range(n_rows):
            for j in zero_indexs:
                matrix[i][j] = 0 

s = Solution()
s.setZeroes([[0],[1]])
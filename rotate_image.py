class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if matrix is None or len(matrix) == 0:
        	return

        n = len(matrix[0])
        for i in range(n):
        	for j in range(i ,n):
        		print i,j
        		matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        print matrix

s = Solution()
s.rotate([[1,2],[3,4]])
class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        Solution.ret = []
        self.DFS(0, [], A)
        return Solution.ret.sort()

    def DFS(self, start, path, A):
    	if start + A[start] >= len(A) -1:
    		return Solution.ret.append(path)
    	for i in range(max(0,start - A[start]), min(len(A),start + A[start])):
    		if i not in path:
    			self.DFS(i, path + [i], A)

s = Solution()
t = s.jump([2, 5, 1, 1, 3, 9, 1 , 5, 3])
print t
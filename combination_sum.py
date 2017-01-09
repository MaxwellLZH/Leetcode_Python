class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
    	Solution.ret  = []
    	candidates.sort()
    	self.DFS(candidates,target, 0, [])
    	return Solution.ret

    def DFS(self, candidates, target, start, values):
    	if target == 0:
    		return Solution.ret.append(values)
    	for i in range(start, len(candidates)):
    		if candidates[i] > target:
    			return
    		self.DFS(candidates, target - candidates[i], i + 1, values + [candidates[i]])


s = Solution()
t = s.combinationSum([1,3,4,5, 9,6], 10)
print t
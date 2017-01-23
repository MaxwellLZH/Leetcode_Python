class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.ret = []
        self.dfs(nums, 0, [])
        return self.ret


    def dfs(self, nums, start, value):
        if value not in self.ret:
            self.ret.append(value)
        for i in xrange(start, len(nums)):
            self.dfs(nums, i + 1, value + [nums[i]])
    

s = Solution()
t = s.subsetsWithDup([1,2,2])
print t
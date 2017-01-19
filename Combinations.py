class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.ret = []
        self.dfs(nums, 0, len(nums), [])
        return self.ret
    

    def dfs(self, nums, start, length, value):
        self.ret.append(value)
        for i in range(start, length):
            self.dfs(nums, i + 1, length, value + [nums[i]])

s = Solution()
t = s.subsets([1,2,3])
print t
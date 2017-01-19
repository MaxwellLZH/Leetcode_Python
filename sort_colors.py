class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.ret = []
        self.dfs(n, 1, 0, k, [])
        return self.ret

    def dfs(self, n, start, count,k, value):
        if count == k:
            return self.ret.append(value)
        for i in range(start, n+1):
            self.dfs(n, i + 1, count + 1, k, value + [i])


s = Solution()
t = s.combine(4,2)
print t
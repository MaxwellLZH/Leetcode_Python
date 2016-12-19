class Solution:
    ret = []
    def dfs(self, left, right, item):
        if right < left:
            return 
        if left == 0 and right == 0 :
            self.ret.append(item)
        if left > 0:
            self.dfs(left-1, right, item + '(')
        if right > 0:
            self.dfs(left, right-1, item + ')')

    def generateParenthesis(self, n):
        if n == 0:
            return []
        else:
            self.dfs(n, n, '')
        print self.ret

s = Solution()
s.generateParenthesis(1)

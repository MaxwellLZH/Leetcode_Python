import math

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        ret = []
        candidate = range(1, n + 1)
        walker = n - 1
        population = k
        for i in range(n-1):
        	pos = population / math.factorial(walker)
        	print 'candidate: ', candidate
        	print 'position: ', pos
        	ret.append(candidate.pop(pos))
        	population = k % math.factorial(walker)
        	walker -= 1
        	print 'return: ', ret
        	print '================='
        ret.append(candidate[0])
        print ret

s = Solution()
s.getPermutation(3, 3)
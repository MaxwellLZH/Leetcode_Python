class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ret = [0]
        for i in range(n):
            new_bit = (1 <<i) + ret[-1] 
            ret.append(new_bit)
        for i in range(n -1):
            new_bit = ret[-1] - (1 << i)
            ret.append(new_bit)
        print ret

s = Solution()
s.grayCode(2)
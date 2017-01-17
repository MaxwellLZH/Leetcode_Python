class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = int(''.join([str(i) for i in digits]))
        num += 1
        ret = [int(i) for i in list(str(num))]
        return ret

s = Solution()
t = s.plusOne([1,2,3])
print t
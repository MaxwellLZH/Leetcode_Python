#reverse integer

class Solution(object):
    def reverse(self, x):
        negative = True if x < 0 else False
        ret = int(str(abs(x))[::-1])
        if ret  > 2**31:
            return 0
        elif negative:
            return -1 * ret
        else:
            return ret


s = Solution()
s.reverse(321)

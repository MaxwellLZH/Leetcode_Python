class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        INT_MAX = 2147483647

        if divisor == 0:
            raise ValueError('Error')
        if dividend == 0:
            return 0

        if cmp(dividend, 0) != cmp(divisor, 0):
            negative = True
        else:
            negative = False

        dividend, divisor = abs(dividend), abs(divisor)
        if dividend < divisor:
            return 0

        res, bits = 0, 31
        while bits >= 0:
            if dividend >= divisor << bits:
                dividend -= divisor << bits
                res += 1 << bits
            bits -= 1
        
        if negative:
            res = -1 * res
        if res > INT_MAX:
            return INT_MAX
        
        return res

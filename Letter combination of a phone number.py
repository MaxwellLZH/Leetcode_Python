#Letter combination of a phone number

from itertools import product

class Solution(object):
    def letterCombinations(self, digits):
        if len(digits) == 0:
            return []
        
        letters = ['','1','abc','def','ghi','jkl','mno', 'pqrs', 'tuv', 'wxyz']
        ret = []
        temp = []
        for i in digits:
            temp.append(letters[int(i)])
        ret = list(product(*temp))
        ret = [''.join(x) for x in ret]
        return ret

#s = Solution()
#s.letterCombinations('23')

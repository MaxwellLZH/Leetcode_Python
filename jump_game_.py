class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        len_list = [len(w) for w in s.split() if w.isalpha()]
        if len(len_list) == 0:
        	return 0
        return len_list[-1]

s = Solution()
t = s.lengthOfLastWord(' a')
print t

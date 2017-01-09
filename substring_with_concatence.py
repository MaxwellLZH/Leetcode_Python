from itertools import permutations

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        
        possible_combinations = [''.join(i) for i in permutations(words)]
        word_length = len(possible_combinations[0])
        string_length = len(s)
        
        if string_length < word_length:
            return []

        start, end = 0, word_length
        res = []
        while end <= string_length:
            if s[start:end] in possible_combinations:
                res.append(start)
            start += 1
            end += 1
        return res

s = Solution()
t = s.findSubstring('ggasstalkjsdstas', ['as','st'])
print t
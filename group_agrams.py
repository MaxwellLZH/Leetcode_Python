from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ret = defaultdict(list)
        for i in strs:
        	key = ''.join(sorted(i))
        	ret[key].append(i)
        return ret.values()

s = Solution()
t = s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print t
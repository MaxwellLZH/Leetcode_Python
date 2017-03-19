class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1_list = [int(x) for x in version1.split('.')]
        v2_list = [int(x) for x in version2.split('.')]

        len_diff = abs(len(v1_list) - len(v2_list))
        if len(v1_list) > len(v2_list):
        	v2_list.extend([0] * len_diff)
        elif len(v1_list) < len(v2_list):
        	v1_list.extend([0] * len_diff)

        for i in range(len(v1_list)):
        	if v1_list[i] < v2_list[i]:
        		return -1
        	elif v1_list[i] > v2_list[i]:
        		return 1
        	else:
        		continue

        return 0



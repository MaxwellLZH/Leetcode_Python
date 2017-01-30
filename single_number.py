class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        cur = 0
        if length == 1:
        	return cur[-1]
        while cur <= length -2:
        	if nums[cur] != nums[cur + 1]:
        		return nums[cur]

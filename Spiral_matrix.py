class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ret = False
        boundary = 0 
        for pos in range(len(nums)):
        	boundary = max(boundary, pos + nums[pos])
        	if boundary >= len(nums) - 1:
        		return True
        	if pos + 1 > boundary:
        		return False
        return ret


s = Solution()
t = s.canJump([3,2,1,0,4])
print t
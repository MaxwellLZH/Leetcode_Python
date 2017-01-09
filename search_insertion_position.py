class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0 or target < nums[0]:
        	return 0

        left, right = 0, len(nums) -1
        while left <= right:
        	mid = (left + right) // 2
        	if nums[mid] == target:
        		return mid
        	elif nums[mid] > target:
        		right = mid - 1
        	else:
        		left = mid + 1

        return left 


s = Solution()
t = s.searchInsert([0,1,2,5,6, 9, 10 ], 3)
print t 
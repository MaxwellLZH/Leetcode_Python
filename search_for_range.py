class Solution(object):
	def searchRange(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		index = None
		if len(nums) == 0:
			return [-1, -1]
		left, right = 0, len(nums) - 1
		if nums[left] == target:
			index = left
		if nums[right] == target:
			index = right
		#binary search
		while left <= right:
			mid = (left + right) // 2 
			if nums[mid] == target:
				index = mid
				break
			elif nums[mid] < target:
				left = mid + 1
			else:
				right = mid - 1

		#found 
		print index
		if index is not None:
			left_i, right_i = index, index
			while left_i >= 1 and nums[left_i -1] == target:
				left_i -= 1
			while right_i < len(nums) -1 and nums[right_i +1] == target:
				right_i += 1
			return [left_i, right_i]
		else:
			return [-1, -1]




s  =Solution()
t = s.searchRange([5,7,7,8,8,10],8)
print t

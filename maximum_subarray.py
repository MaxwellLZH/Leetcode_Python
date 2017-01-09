import numpy as np

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [i for i in nums if i != 0]
        alternate_array = []
       	partial_sum = 0
       	for i in range(len(nums)):
       		partial_sum += nums[i]
       		#last one
       		if i + 1 == len(nums):
       			alternate_array.append(partial_sum)
       			break
       		#end of consecutive positives or negatives
       		if nums[i] * nums[i + 1] < 0:
       			alternate_array.append(partial_sum)
       			partial_sum = 0

       	
       	ret = max(alternate_array)
       	max_index = np.argmax(ret)
       	while alternate_array[max_index] > 0:
       		partial_sum = alternate_array[max_index]
       		i = j = 1
       		while max_index - i > 0 and 


s = Solution()
s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
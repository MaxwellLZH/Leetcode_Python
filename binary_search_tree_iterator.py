class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count_dict = {}
        thre = len(nums)/ 2
        for num in nums:
            count_dict[num] = count_dict.get(num, 0) + 1
            if count_dict[num] > thre:
                return num

    
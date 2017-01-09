class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        ascend = True
        for i in range(length-2, -1, -1):
            minimum = None
            
            for j in range(i+1, length):
                if nums[j] > nums[i]:
                    if minimum:
                        minimum = j if nums[j] < nums[minimum] else minimum
                    else:
                        minimum = j

            if minimum:
                nums[i], nums[minimum] = nums[minimum], nums[i]
                ascend = False
                break


        if ascend:
            nums.sort()
        print nums

s = Solution()
s.nextPermutation([1,3,4,5])

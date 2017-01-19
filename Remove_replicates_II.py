class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) /2
            print left, right
            if nums[mid] == target:
                return True
            if nums[mid] < target:
                if nums[right] < target:
                    right = mid
                else:
                    left = mid
            if nums[mid] > target:
                if nums[left] > target:
                    left = mid
                else:
                    right = mid
        return False

s = Solution()
t = s.search([4, 5, 6, 7, 8, 0, 1], 9)
print t
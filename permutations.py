class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        Solution.ret = []


    def permute(self, nums):
        # write your code here
        def _permute(result, temp, nums):
            if nums == []:
                result += [temp]
            else:
                for i in range(len(nums)):
                    _permute(result, temp + [nums[i]], nums[:i] + nums[i+1:])

        if nums is None:
            return []
        
        if nums is []:
            return [[]]

        result = []
        _permute(result, [], sorted(nums))
        return result


s = Solution()
t = s.permute([1,2,3])
print t


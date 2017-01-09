from numpy import diff

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) == 0:
        	return 0
        max_height = max(height)
        ret = 0
        for i in range(max_height, 0, -1):
        	position = [j for j in range(len(height)) if height[j] >= i]
        	ret += self.trap_layer(position)
        return ret


    def trap_layer(self, position):
    	return sum(diff(position) -1)


s = Solution()
t = s.trap([2,0,2 ])
print t
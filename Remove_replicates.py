class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        max_area = heights[0]
        for pos in range(len(heights)):
            width = self.find_width(pos, heights)
            max_area = max(max_area, width * heights[pos])
        return max_area


    def find_width(self, pos, heights):
        #given a position find the corresponding width
        left, right = pos, pos
        while (left -1) >= 0 and heights[left -1] >= heights[pos]:
            left -= 1
        while (right + 1)<= (len(heights) - 1) and heights[right+1] >= heights[pos]:
            right += 1
        return right - left + 1

s = Solution()
t = s.largestRectangleArea([2,1,5,6,2,3])
print t
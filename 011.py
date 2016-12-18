#container with most water
#two pointer moving towards middle O(n) time

class Solution(object):
    def area(self, x, left_pos, right_pos):
        width = right_pos - left_pos
        height = min(x[left_pos], x[right_pos])
        return width * height


    def maxArea(self, height):
        left_pos, right_pos = 0, len(height) - 1
        current_area, max_area = 0, 0
        while left_pos < right_pos:
            current_area = self.area(height, left_pos, right_pos)
            if current_area > max_area:
                max_area = current_area
            if height[left_pos] > height[right_pos]:
                right_pos -= 1
            else:
                left_pos += 1
        return max_area


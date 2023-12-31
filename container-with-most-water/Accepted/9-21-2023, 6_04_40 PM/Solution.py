// https://leetcode.com/problems/container-with-most-water

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        max_area = 0
        while left < right:
            h = min(height[right],height[left])
            w = right - left
            area = h*w
            if area > max_area:
                max_area = area
            if height[left] <= height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
        return max_area



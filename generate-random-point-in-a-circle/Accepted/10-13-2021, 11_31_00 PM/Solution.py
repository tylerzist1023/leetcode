// https://leetcode.com/problems/generate-random-point-in-a-circle

import random as r
import math as m

class Solution:
    radius = 0
    x_center = 0
    y_center = 0
    
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self):
        rand_radius = self.radius*m.sqrt(r.uniform(0,1))
        rand_theta = m.pi*2*r.uniform(0,1)

        return [rand_radius*m.cos(rand_theta) + self.x_center, rand_radius*m.sin(rand_theta) + self.y_center]

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
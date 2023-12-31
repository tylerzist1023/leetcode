// https://leetcode.com/problems/find-the-duplicate-number

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tortoise = 0
        hare = 0
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        tortoise2 = 0
        while True:
            tortoise = nums[tortoise]
            tortoise2 = nums[tortoise2]
            if tortoise == tortoise2:
                break

        return tortoise
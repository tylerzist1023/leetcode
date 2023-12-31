// https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii

class Solution:
    def removeDuplicates(self, nums: list) -> int:
        i = j = k = 2
        n = len(nums)
        if n <= k:
            return n
        while(j < n):
            if nums[j] != nums[i-k]:
                nums[i] = nums[j]
                i += 1
            j += 1
        return i
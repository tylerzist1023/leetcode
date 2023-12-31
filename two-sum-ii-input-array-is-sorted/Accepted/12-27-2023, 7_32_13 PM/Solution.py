// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1

        while left != right:
            s = numbers[left] + numbers[right]
            if s == target:
                return [left+1, right+1]
            if s > target:
                right -= 1
            if s < target:
                left += 1
        
        return []
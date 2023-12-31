// https://leetcode.com/problems/search-a-2d-matrix

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix[0])
        m = len(matrix)

        bottom = m-1
        top = 0

        while bottom-top > 1:
            mid = (top + bottom) // 2
            row = matrix[mid]
            if target < row[0]:
                bottom = mid-1
            elif row[-1] < target:
                top = mid+1
            else:
                return self.search(row, target)
        
        if matrix[top][0] <= target and target <= matrix[top][-1]:
            return self.search(matrix[top], target)
        elif matrix[bottom][0] <= target and target <= matrix[bottom][-1]:
            return self.search(matrix[bottom], target)
        return False
        
        
    def search(self, nums: List[int], target: int) -> bool:
        start = 0
        end = len(nums) - 1

        while end - start > 1:
            mid = (end + start) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1

        if nums[start] == target:
            return True
        if nums[end] == target:
            return True

        return False
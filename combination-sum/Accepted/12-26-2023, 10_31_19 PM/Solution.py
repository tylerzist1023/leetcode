// https://leetcode.com/problems/combination-sum

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(nums):
            if sorted(nums) in res:
                return
            if sum(nums) == target:
                res.append(sorted(nums.copy()))
                return
            if sum(nums) > target:
                return

            for candidate in candidates:
                nums_copy = nums.copy()
                nums_copy.append(candidate)
                dfs(nums_copy)

        dfs([])
        return res
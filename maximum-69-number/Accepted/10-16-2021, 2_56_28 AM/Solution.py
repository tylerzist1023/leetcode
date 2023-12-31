// https://leetcode.com/problems/maximum-69-number

class Solution:
    def maximum69Number(self, num: int) -> int:
        num_s = str(num)
        for i in range(len(num_s)):
            if num_s[i] == '6':
                return int((num_s[:i] + '9' + num_s[i+1:]))
        return num
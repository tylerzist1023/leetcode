// https://leetcode.com/problems/maximum-69-number

class Solution:
    def maximum69Number(self, num: int) -> int:
        power = 3
        while 10**power > num:
            power -= 1
        test = (10**power)*3
        while test > 0:
            if num+test < 10**(power+1):
                return num+test
            test //= 10
        return num
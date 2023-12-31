// https://leetcode.com/problems/maximum-69-number

class Solution:
    def maximum69Number(self, num: int) -> int:
        power = 3
        while 10**power > num:
            power -= 1
        power_val = (10**(power+1))
        test = power_val*3

        while test > 0:
            if num+test < power_val:
                return num+test
            test //= 10
        return num
// https://leetcode.com/problems/maximum-69-number

class Solution:
    def maximum69Number(self, num: int) -> int:
        power = 0
        num2 = num//10
        while num2 != 0:
            num2 //= 10
            power += 1
        power_val = (10**power)

        test = power_val*3
        while test > 0:
            if num+test < power_val*10:
                return num+test
            test //= 10
        return num
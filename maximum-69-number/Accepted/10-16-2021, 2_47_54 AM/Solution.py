// https://leetcode.com/problems/maximum-69-number

import math as m

class Solution:
    def maximum69Number(self, num: int) -> int:
        power_val = 10**int(m.log10(num*10))
        print('\n',power_val)

        test = power_val*3
        while test > 0:
            if num+test < power_val:
                return num+test
            test //= 10
        return num
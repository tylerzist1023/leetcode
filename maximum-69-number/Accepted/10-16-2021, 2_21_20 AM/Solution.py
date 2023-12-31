// https://leetcode.com/problems/maximum-69-number

class Solution:
    def maximum69Number (self, num: int) -> int:
        num2 = num
        digit_index = 0
        has_6 = False
        i = 0
        while num2 > 0:
            print(num2 % 10)
            if (num2 % 10) == 6:
                has_6 = True
                digit_index = i
            num2 //= 10 # double slash to do integer division
            i += 1
        return (num + (3*(10**digit_index)) if has_6 else num)
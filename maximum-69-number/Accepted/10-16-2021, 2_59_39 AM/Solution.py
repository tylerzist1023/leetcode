// https://leetcode.com/problems/maximum-69-number

class Solution:
    def maximum69Number(self, num: int) -> int:
        test = 10000
        while test != 0:
            if (num//test) % 10 == 6:
                num += 3*test
                break
            test //= 10
        return num
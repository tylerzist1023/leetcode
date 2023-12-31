// https://leetcode.com/problems/three-divisors

class Solution:
    def isThree(self, n: int) -> bool:
        divisors = 2
        for i in range(2,(n//2)+1):
            divisors += (n % i == 0)
        return divisors == 3
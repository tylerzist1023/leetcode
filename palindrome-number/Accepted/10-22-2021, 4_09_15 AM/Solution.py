// https://leetcode.com/problems/palindrome-number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False

        xs = str(x)
        if xs == xs[::-1]:
            return True
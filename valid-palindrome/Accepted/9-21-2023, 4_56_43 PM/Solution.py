// https://leetcode.com/problems/valid-palindrome

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        trimmed = ""
        for c in s:
            if str(c).isalnum():
                trimmed += str(c).lower()
        
        for i in range(len(trimmed)):
            if trimmed[i] != trimmed[len(trimmed)-i-1]:
                return False
        return True
        
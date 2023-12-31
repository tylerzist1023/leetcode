// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left, right = 0,0
        letters = {}
        max_window = 0
        while left < len(s) and right < len(s):
            if letters.has_key(s[right]) and letters[s[right]] >= left:
                left = letters[s[right]]+1

            letters[s[right]] = right

            window = right-left+1
            if window > max_window:
                max_window = window
            
            right+=1

        return max_window
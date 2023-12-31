// https://leetcode.com/problems/longest-repeating-character-replacement

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left,right=0,0
        max_window = 0
        letters = {}
        while left<len(s) and right<len(s):
            if letters.has_key(s[right]):
                    letters[s[right]] += 1
            else:
                letters[s[right]] = 1
            found_repeating_string = False
            for l in letters:
                window = right - left + 1
                same_chars = window
                same_chars -= letters[l] + k
                if same_chars <= 0:
                    found_repeating_string = True
                    if window > max_window:
                        max_window = window
                    break
            if not found_repeating_string:
                if letters.has_key(s[left]):
                    letters[s[left]] -= 1
                left += 1
            right += 1
        return max_window
            
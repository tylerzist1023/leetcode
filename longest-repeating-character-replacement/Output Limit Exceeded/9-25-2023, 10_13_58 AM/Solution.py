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
        while left<len(s) and right<len(s):
            letters = {}
            for c in s[left:right+1]:
                if letters.has_key(c):
                    letters[c] += 1
                else:
                    letters[c] = 1
            found_repeating_string = False
            for l in letters:
                print(s[left:right])
                window = right - left + 1
                same_chars = window
                same_chars -= letters[l] + k
                if same_chars <= 0:
                    found_repeating_string = True
                    print(letters[l],same_chars)
                    if window > max_window:
                        max_window = window
                    break
            if not found_repeating_string:
                left += 1
            right += 1
        return max_window
            
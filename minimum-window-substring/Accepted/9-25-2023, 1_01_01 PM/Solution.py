// https://leetcode.com/problems/minimum-window-substring

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        left,right = 0,0
        min_left,min_window=-1,len(s)

        requirements = {}
        for c in t:
            if not requirements.has_key(c):
                requirements[c] = 1
            else:
                requirements[c] += 1

        while left<len(s) and not requirements.has_key(s[left]):
            left += 1
            right += 1

        while left<len(s) and right<len(s):
            if requirements.has_key(s[right]):
                requirements[s[right]] -= 1
                while left <= right and requirements.has_key(s[left]) and requirements[s[left]] < 0:
                    requirements[s[left]] += 1
                    left += 1
                while left <= right:
                    if requirements.has_key(s[left]) and requirements[s[left]] < 0:
                        requirements[s[left]] += 1
                        left += 1
                    elif not requirements.has_key(s[left]):
                        left += 1
                    else:
                        break
                
                requirements_satisfied = True
                for r in requirements:
                    if requirements[r] > 0:
                        requirements_satisfied = False
                        break
                if requirements_satisfied:
                    window = right - left + 1
                    if window <= min_window:
                        min_window = window
                        min_left = left
                    requirements[s[left]] += 1
                    left += 1
                    while left <= right and requirements.has_key(s[left]) and requirements[s[left]] < 0:
                            requirements[s[left]] += 1
                            left += 1
                    while left <= right:
                        if requirements.has_key(s[left]) and requirements[s[left]] < 0:
                            requirements[s[left]] += 1
                            left += 1
                        elif not requirements.has_key(s[left]):
                            left += 1
                        else:
                            break

            right += 1
        if min_left == -1:
            return ""
        return s[min_left:min_left+min_window]

                


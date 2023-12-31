// https://leetcode.com/problems/reformat-the-string

class Solution:
    def reformat(self, s: str) -> str:
        result = ""
        numcnt = 0
        ltrcnt = 0
        ls = len(s)
        for c in s:
            numcnt += c.isnumeric()
            ltrcnt += c.isalpha()
        lookingfor = ltrcnt < numcnt # False = number, True = letter
        i = 0
        found = False
        while len(s) > 0:
            if (s[i].isnumeric() and lookingfor) or (s[i].isalpha() and not lookingfor):
                lookingfor = not lookingfor
                result += s[i]
                s = s[:i] + s[i+1:]
                i -= 1
                found = True
            i = (i+1) % max(1,len(s))
            if i == 0:
                if not found:
                    break
                found = False
        return result if len(result) == ls else ''
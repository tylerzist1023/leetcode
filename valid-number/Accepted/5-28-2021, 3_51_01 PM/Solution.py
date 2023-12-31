// https://leetcode.com/problems/valid-number

import re

class Solution(object):
    def isNumber(self, s):
        s = s.strip()
        return re.match("^[+-]?(\d+|\d+\.\d*|\d*\.\d+)([eE][+-]?\d+)?$",s)
// https://leetcode.com/problems/valid-number

import re

class Solution(object):
    def isNumber(self, s):
        return re.match("^(\s+)?[+-]?(\d+|\d+\.\d*|\d*\.\d+)([eE][+-]?\d+)?$",s)
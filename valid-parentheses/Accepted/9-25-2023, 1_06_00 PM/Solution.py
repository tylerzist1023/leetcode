// https://leetcode.com/problems/valid-parentheses

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c == '(':
                stack.append('(')
            elif c == '[':
                stack.append('[')
            elif c == '{':
                stack.append('{')
            if c == ')':
                if len(stack) == 0 or stack[len(stack)-1] != '(':
                    return False
                stack = stack[:len(stack)-1]
            elif c == ']':
                if len(stack) == 0 or stack[len(stack)-1] != '[':
                    return False
                stack = stack[:len(stack)-1]
            elif c == '}':
                if len(stack) == 0 or stack[len(stack)-1] != '{':
                    return False
                stack = stack[:len(stack)-1]
            
        return len(stack) == 0
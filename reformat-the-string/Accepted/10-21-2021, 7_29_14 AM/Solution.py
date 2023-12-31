// https://leetcode.com/problems/reformat-the-string

class Solution:
    def reformat(self, s: str) -> str:
        letters = ""
        numbers = ""

        for c in s:
            if c.isnumeric(): numbers += c
            elif c.isalpha(): letters += c
        
        if abs(len(letters) - len(numbers)) > 1: return ""

        result = ""
        if len(letters) > len(numbers):
            result += letters[0]
            for i in range(len(numbers)):
                result += numbers[i]
                result += letters[i+1]
        elif len(letters) < len(numbers):
            result += numbers[0]
            for i in range(len(letters)):
                result += letters[i]
                result += numbers[i+1]
        else:
            for i in range(len(numbers)):
                result += letters[i]
                result += numbers[i]
        
        return result
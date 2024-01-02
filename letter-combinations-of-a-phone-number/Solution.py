class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        res = []

        phone = ['',       'abc','def',
                 'ghi','jkl','mno',
                 'pqrs','tuv','wxyz']

        text = []
        def dfs(i):
            if i >= len(digits):
                res.append("".join(text))
                return

            for c in phone[int(digits[i])-1]:
                text.append(c)
                dfs(i+1)
                text.pop()
            
        dfs(0)
        return res
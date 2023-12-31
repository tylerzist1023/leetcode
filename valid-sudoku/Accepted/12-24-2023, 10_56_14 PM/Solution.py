// https://leetcode.com/problems/valid-sudoku

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        for i in range(9):
            nums = set([])
            for j in range(9):
                if board[i][j] == '.':
                        continue
                elif board[i][j] not in nums:
                    nums.add(board[i][j])
                else:
                    print(i, j, board[i][j], nums)
                    return False
        
        for j in range(9):
            nums = set([])
            for i in range(9):
                if board[i][j] == '.':
                        continue
                elif board[i][j] not in nums:
                    nums.add(board[i][j])
                else:
                    print(i, j, board[i][j], nums)
                    return False

        starts = [(0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6)]

        for start in starts:
            nums = set([])
            for i in range(start[0],start[0]+3):
                for j in range(start[1],start[1]+3):
                    if board[i][j] == '.':
                        continue
                    elif board[i][j] not in nums:
                        nums.add(board[i][j])
                    else:
                        print(i, j, board[i][j], nums)
                        return False
            
        return True
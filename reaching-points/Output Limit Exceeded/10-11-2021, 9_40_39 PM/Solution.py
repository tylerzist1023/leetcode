// https://leetcode.com/problems/reaching-points

class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        cx = tx
        cy = ty
        while cx != sx or cy != sy:
            print(cx,cy)

            if cx > cy:
                cx -= cy
            elif cx < cy:
                cy -= cx
            else:
                return False
            
            if cx < 1 or cy < 1:
                return False
        return True
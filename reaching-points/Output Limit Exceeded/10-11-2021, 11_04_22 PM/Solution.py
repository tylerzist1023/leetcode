// https://leetcode.com/problems/reaching-points

class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        if sx > tx or sy > ty: # can't lower the start values, only raise
            return False
        if tx == 1 or ty == 1: # saves time on inputs like 1 1 10^9 1
            return True

        cx = tx
        cy = ty
        while cx != sx or cy != sy:
            if cx > cy:
                times = max(int(cx/cy)-1,1)
                if cy == 1:
                    times = 1
                cx -= cy*times
                if times > 1 and cx < sx:
                    cx = sx
            elif cx < cy:
                times = max(int(cy/cx)-1,1)
                if cx == 1:
                    times = 1
                cy -= cx*times
                if times > 1 and cy < sy:
                    cy = sy
            else:
                return False
            
            print(cx,cy)

            if cx < sx or cy < sy:
                return False
        return True
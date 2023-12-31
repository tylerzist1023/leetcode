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
            print(cx, cy)

            if cx > cy:
                print('<')
                times = max(1,int(cx/cy)-1)
                if times > 0:
                    cx -= cy*times
                    if cx < sx and abs(cx-sx) % times == 0:
                        cx = sx
            elif cx < cy:
                print('>')
                times = max(1,int(cy/cx)-1)
                cy -= cx*times
                if cy < sy and abs(cy-sy) % times == 0:
                    cy = sy
            else:
                return False
            
            print(cx, cy)
            if cx < sx or cy < sy:
                return False
            print(cx, cy)
        return True
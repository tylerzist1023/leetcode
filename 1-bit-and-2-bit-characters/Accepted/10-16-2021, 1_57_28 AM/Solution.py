// https://leetcode.com/problems/1-bit-and-2-bit-characters

class Solution:
    def isOneBitCharacter(self, bits) -> bool:
        # fuck i'm stupid
        ret = True
        for bit in bits[-2::-1]:
            if bit == 1: ret = not ret
            else: break
        return ret
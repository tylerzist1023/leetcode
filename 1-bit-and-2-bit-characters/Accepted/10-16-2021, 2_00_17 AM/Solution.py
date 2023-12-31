// https://leetcode.com/problems/1-bit-and-2-bit-characters

class Solution:
    def isOneBitCharacter(self, bits) -> bool:
        # fuck i'm stupid
        ones = 0
        for bit in bits[-2::-1]:
            if bit == 1: ones += 1
            else: break
        return (ones % 2) == 0
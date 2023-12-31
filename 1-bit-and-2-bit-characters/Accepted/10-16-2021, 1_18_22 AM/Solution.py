// https://leetcode.com/problems/1-bit-and-2-bit-characters

class Solution:
    def isOneBitCharacter(self, bits) -> bool:
        i = 0
        while i < len(bits):
            print(bits[i])
            if bits[i] == 1:
                if i+2 == len(bits):
                    return False
                i += 1
            i += 1
        return True
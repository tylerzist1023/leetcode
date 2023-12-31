// https://leetcode.com/problems/1-bit-and-2-bit-characters



bool isOneBitCharacter(int* bits, int bitsSize)
{
    int onesUntilZero = 0;
    for(register i = bitsSize - 2; i >= 0 && bits[i] != 0; i--)
        onesUntilZero++;
    return (onesUntilZero % 2) == 0;
}
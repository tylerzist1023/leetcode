// https://leetcode.com/problems/power-of-three

static const int max_powerof3 = 1162261467; // maximum power that can be represented by a signed 32-bit int, equates to 3^20
bool isPowerOfThree(int n)
{
    if(n <= 0) return false;
    return max_powerof3 % n == 0;
}
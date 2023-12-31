// https://leetcode.com/problems/power-of-three

static const int max_powerof3 = 1162261467;
bool isPowerOfThree(int n)
{
    if(n <= 0 || n > max_powerof3) return false;
    return max_powerof3 % n == 0;
}
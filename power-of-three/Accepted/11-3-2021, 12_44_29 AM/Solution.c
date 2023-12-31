// https://leetcode.com/problems/power-of-three

bool isPowerOfThree(int n)
{
    if(n == 0) return false;
    while(1)
    {
        if(n == 1) return true;
        if((n / 3) * 3 == n) n/=3;
        else return false;
    }
}
// https://leetcode.com/problems/maximum-69-number

int maximum69Number (int num)
{
    uint_fast32_t test = 10000;
    while(test > 0)
    {
        if(num/test % 10 == 6)
        {
            return num+3*test;
        }
        test /= 10;
    }
    return num;
}
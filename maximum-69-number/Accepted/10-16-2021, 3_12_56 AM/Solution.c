// https://leetcode.com/problems/maximum-69-number

int maximum69Number (int num)
{
    register test = 10000;
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
// https://leetcode.com/problems/maximum-69-number

#include <stdlib.h>

int maximum69Number (int num)
{
    char num_s[5];
    itoa(num, num_s, 10);
    for(char* it = &num_s; it != '\0'; it++)
    {
        if(*it == '6')
        {
            *it = '9';
            break;
        }
    }
    return atoi(&num_s);
}
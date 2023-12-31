// https://leetcode.com/problems/maximum-69-number

#include <stdlib.h>
#include <stdio.h>

int maximum69Number (int num)
{
    char num_s[5];
    sprintf(num_s, "%d", num);
    for(char* it = &num_s; *it != '\0'; it++)
    {
        if(*it == '6')
        {
            *it = '9';
            break;
        }
    }
    return atoi(&num_s);
}
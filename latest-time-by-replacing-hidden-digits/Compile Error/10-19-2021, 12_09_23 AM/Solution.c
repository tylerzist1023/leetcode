// https://leetcode.com/problems/latest-time-by-replacing-hidden-digits



char * maximumTime(char * time)
{
    if(time[0] == '?')
    {
        if(time[1] <= '3' || time[1] == '?') time[0] = '2';
        else time[0] = '1';
    }
    if(time[1] == '?')
    {
        if(time[0] <= '1') time[1] = '9';
        else time[1] = '3';
    }
    if(time[3] == '?') time[3] = '5';
    if(time[4] == '?') time[4] = '9';
}
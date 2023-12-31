// https://leetcode.com/problems/latest-time-by-replacing-hidden-digits



char * maximumTime(char * time)
{
    for(int i = 0; i < 5; i++)
    {
        if(time[i] == '?')
        {
            if(i == 0)
            {
                if(time[1] <= '3' || time[1] == '?') time[0] = '1';
                else time[0] = '2';
            }
            if(i == 1)
            {
                if(time[0] == '1') time[1] = '9';
                else time[1] = '3';
            }
            if(i == 3) time[i] = '5';
            if(i == 4) time[i] = '9';
        }
    }
}
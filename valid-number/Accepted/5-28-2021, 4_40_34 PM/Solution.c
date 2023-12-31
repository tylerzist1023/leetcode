// https://leetcode.com/problems/valid-number



bool isNumber(char* s)
{
    size_t seek = 0;
    bool dot = false;
    bool e = false;

    while(s[seek] == ' ') seek++; // check whitespace
    if(s[seek] == '-' || s[seek] == '+') seek++; // check for optional plus or minus

    if(s[seek] == '.')
    {
        dot = true;
        seek++;
    }
    
    while(s[seek] >= '0' && s[seek] <= '9') 
    {
        if(seek >= strlen(s)-1) return true;
        
        seek++;

        if(s[seek] == '.')
        {
            if(dot || e) break;
            dot = true;

            seek++;
            
            if(seek >= strlen(s))
            {
                return true;
            }
        }
        if(s[seek] == 'e' || s[seek] == 'E')
        {
            if(e) break;
            e = true;

            seek++;
            
            if(s[seek] == '\0') break;
            else if(s[seek] == '-' || s[seek] == '+') seek++; // check for optional plus or minus
        }
    }
    
    return false;
}
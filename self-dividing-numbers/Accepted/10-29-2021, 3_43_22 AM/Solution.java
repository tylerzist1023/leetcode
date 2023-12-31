// https://leetcode.com/problems/self-dividing-numbers

import java.util.ArrayList;
import java.util.List;

class Solution
{
    public List<Integer> selfDividingNumbers(int left, int right)
    {
        ArrayList<Integer> nums = new ArrayList<>();

        for(int i = left; i <= right; i++)
        {
            boolean isSelfDividing = true;
            int divisor = i;
            while(divisor > 0)
            {
                if(divisor % 10 == 0 || i % (divisor % 10) != 0)
                {
                    isSelfDividing = false;
                    break;
                }
                divisor /= 10;
            }
            if(isSelfDividing) nums.add(i);
        }

        return nums;
    }
}
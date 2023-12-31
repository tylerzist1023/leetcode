// https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors

class Solution
{
    public int[] rearrangeArray(int[] nums)
    {
        int i = 1;
        while(i < nums.length - 1)
        {
            double avg = (nums[i - 1] + nums[i + 1]) / 2.0;
            if (nums[i] == (int) avg)
            {
                int temp = nums[i];
                nums[i] = nums[i + 1];
                nums[i + 1] = temp;
                i-=2;
                if(i < 1) i = 1;
            }
            else i++;
        }
        return nums;
    }
}
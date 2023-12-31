// https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors

class Solution
{
    public int[] rearrangeArray(int[] nums)
    {
        boolean done = false;
        while(!done)
        {
            done = true;
            for (int i = 1; i < nums.length - 1; i++)
            {
                double avg = (nums[i - 1] + nums[i + 1]) / 2.0;
                if (nums[i] == (int) avg)
                {
                    done = false;
                    int temp = nums[i];
                    nums[i] = nums[i + 1];
                    nums[i + 1] = temp;
                }
            }
        }
        return nums;
    }
}
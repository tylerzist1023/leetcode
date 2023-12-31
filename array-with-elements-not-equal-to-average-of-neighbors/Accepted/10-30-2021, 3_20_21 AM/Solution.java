// https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors

class Solution
{
    public int[] rearrangeArray(int[] nums)
    {
        int i = 1;
        while(i < nums.length - 1)
        {
            // check if the average of neighbors matches the current num
            if (2*nums[i] == (nums[i - 1] + nums[i + 1]))
            {
                // if it does, swap the num with the next num
                int temp = nums[i];
                nums[i] = nums[i + 1];
                nums[i + 1] = temp;

                // need to go back in case we create a new scenario in which the prev num's neighbors avg == prev num
                i--;
                if(i < 1) i = 1;
            }
            else i++;
        }
        return nums;
    }
}
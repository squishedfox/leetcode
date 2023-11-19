public class Solution {
    /// <summary>
    ///
    /// </summary>
    /// <see ref="https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150" />
    public int RemoveElement(int[] nums, int val) {
        var actualLength = 0;
        foreach (var num in nums)
        {
            if (num != val)
            {
                nums[actualLength] = num;
                actualLength++;
            }
        }
        return actualLength;
    }
}

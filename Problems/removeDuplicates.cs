public class Solution {
    /// <summary>
    ///  Remove all duplicates in place and return a number which is the new size of the array. The rest of the array can be ignored after "k"
    /// </summary>
    /// <see cref="https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/?envType=study-plan-v2&envId=top-interview-150" />
    public int RemoveDuplicates(int[] nums) {
        var numCounts = new Dictionary<int, int>(); // use a dictionary so we can keep track of the number of times we have seen a number
        var left = 0; // use our own custom index to only incriment when we care
        var actualSize = nums.Length;
        while (left < actualSize)
        {
            var num = nums[left];
            if (!numCounts.ContainsKey(num))
            {
                numCounts.Add(num, 0);
            }
            numCounts[num] += 1;
            if (numCounts[num] == 1)
            {
                left++; // we can continue to move to the left since we have only seen this once
                continue;
            }
            // need to move all the numbers to the left. We have seen this number more
            // than once.
            for (var j = left; j < nums.Length - 1; j++)
            {
                nums[j] = nums[j + 1]; // assign it to the number to the right
            }
            // dont increase the left incriment because we want to hold onto it
            // as the value that we are looking at
            actualSize--;
        }

        return actualSize;
    }
}

public class Solution {
    // see https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/705/hashing/4664/

    /// <summary>
    ///   You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have.
    ///   Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels. 
    ///   Letters are case sensitive, so "a" is considered a different type of stone from "A".
    /// </summary>
    public int NumJewelsInStones(string jewels, string stones) {
        int num = 0;
        foreach (char stone in stones)
        {
            if (jewels.Contains(stone))
            {
                ++num;
            }
        }
        return num;
    }
}

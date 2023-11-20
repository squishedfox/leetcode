public class Solution {
    public int MajorityElement(int[] nums) {
        var majorityDictionary = new Dictionary<int, int>();
        var maxElementNum = int.MinValue;
        var toBeat = (nums.Length / 2);

        foreach (var num in nums)
        {
            if (!majorityDictionary.ContainsKey(num))
            {
                majorityDictionary.Add(num, 0);
            }
            majorityDictionary[num] += 1;
            if (majorityDictionary[num] > toBeat)
            {
                maxElementNum = num;
            }
        }

        return maxElementNum;
    }
}

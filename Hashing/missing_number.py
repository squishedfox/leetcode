class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        """
        Given an array nums containing n distinct numbers in the range `[0, n]`, return the only number in the range that is missing from the array.

        Example 1:

        Input: `nums = [3,0,1]`
        Output: `2`
        Explanation: `n = 3` since there are `3` numbers, so all numbers are in the range `[0,3]`. `2` is the missing number in the range since it does not appear in nums.

        Example 2:

        Input: `nums = [0,1]`
        Output: `2`
        Explanation: `n = 2` since there are `2` numbers, so all numbers are in the range `[0,2]`. `2` is the missing number in the range since it does not appear in nums.

        Example 3:

        Input: `nums = [9,6,4,2,3,5,7,0,1]`
        Output: `8`
        Explanation: `n = 9` since there are `9` numbers, so all numbers are in the range `[0,9]`. `8` is the missing number in the range since it does not appear in nums.

        Constraints:

            n == nums.length
            1 <= n <= 104
            0 <= nums[i] <= n
            All the numbers of nums are unique.

        Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
        """
        num_set = set(nums)
        for i in range(len(nums) + 1):
            if i not in num_set:
                return i
            
        return None

        
def test_missing_number_should_be_2():
    missing_number = Solution().missingNumber([3,0,1])
    assert missing_number == 2, f'Missing number should be "2" but instead found {missing_number}'

    missing_number = Solution().missingNumber([0,1])
    assert missing_number == 2, f'Missing number should be "2" but instead found {missing_number}'
    
def test_missing_number_should_be_8():
    missing_number = Solution().missingNumber([9,6,4,2,3,5,7,0,1])
    assert missing_number == 8, f'Missing number should be "8" but instead found {missing_number}'
    

if __name__ == "__main__":
    test_missing_number_should_be_2()
    test_missing_number_should_be_8()

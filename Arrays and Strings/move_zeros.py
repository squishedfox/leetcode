def moveZeroes(nums: list[int]) -> None:
    """
    Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

    Note that you must do this in-place without making a copy of the array.

    Example 1:

        Input: nums = [0,1,0,3,12]
        Output: [1,3,12,0,0]

    Example 2:

        Input: nums = [0]
        Output: [0]

    :see: https://leetcode.com/problems/move-zeroes/
    """
    right_bounds = 1
    for left_bounds in range(len(nums) - 1):
        if nums[left_bounds] != 0:
            right_bounds += 1
            continue
        
        # keep moving to the right to replace this number with a 0
        while right_bounds < len(nums) and nums[right_bounds] == 0:
            right_bounds += 1
        if right_bounds == len(nums):
            break # we have reached the end
        nums[left_bounds] = nums[right_bounds]
        nums[right_bounds] = 0

input = [0,0,0]

moveZeroes(input)
print(input) # should be [0,0,0]

input = [0,1,0,3,12]

moveZeroes(input)
print(input)  # should be [1,3,12,0,0]

input = [0]
moveZeroes(input)
print(input) # should be [0]

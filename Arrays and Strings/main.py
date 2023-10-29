def longestOnes(nums: list[int], k: int) -> int:
    """
    Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

    Example:
    -------
        Input: nums = `[1,1,1,0,0,0,1,1,1,1,0]`, `k = 2`
        Output: `6`
        Explanation: [1,1,1,0,0,1,1,1,1,1,1]
        Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
    
    Example:
    -------
        Input: `nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]`, `k = 3`
        Output: `10`
        Explanation: `[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]`
        Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
    """
    left = curr = ans = 0
    
    for right in range(len(nums)):
        if nums[right] == 0:
            curr += 1

        # If we have more than k zeros, we need to move the left pointer forward
        # until we have curr <= k so that we have a new set of bounds where there
        # will be at most k zeros

        while curr > k:
            if nums[left] == 0:
                curr -= 1
            left += 1

        ans = max(ans, right - left + 1)
        
    return ans

input = [1,1,1,0,0,0,1,1,1,1,0]
k = 2

print(longestOnes(input, k))

nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3

print(longestOnes(input, k))

# Maximum Average Subarray I
def findMaxAverage(nums: list[int], k: int) -> float:
    """
    Given an array consisting of `n` integers, find the contiguous subarray of given length `k` that has the maximum average value. And you need to output the maximum average value.

    Example:
    -------
        Input: `nums = [1,12,-5,-6,50,3], k = 4`
        Output: `12.75`
        Explanation: `Maximum average is (12-5-6+50)/4 = 51/4 = 12.75`
    """
    cur = ans = 0
    for i in range(k):
        ans += nums[i]
    
    cur = ans
    for right in range(k, len(nums)):
        cur += nums[right] - nums[right - k]
        ans = max(ans, cur)

    return float(ans / k)
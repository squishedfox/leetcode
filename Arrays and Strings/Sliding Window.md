# Sliding Windows

## Summary

Sliding windows contain the constarint of validating that a sub array of values is inside another array of values. For example [1,2,3,4], the sub array [2,3] is starting at the index 1 and ending at the index 2.

## When should you use a sliding window?

**First**, the problem will either explicitly or implicitly define criteria that make a subarray "valid". There are 2 components regarding what makes a subarray valid:

   1. A constraint metric. This is some attribute of a subarray. It could be the sum, the number of unique elements, the frequency of a specific element, or any other attribute.
   2. A numeric restriction on the constraint metric. This is what the constraint metric should be for a subarray to be considered valid.

**Second** the problem will ask you to find valid subarrays in some way.

   1. The most common task you will see is finding the best valid subarray. The problem will define what makes a subarray better than another. For example, a problem might ask you to find the longest valid subarray.
   2. Another common task is finding the number of valid subarrays. We will take a look at this later in the article.


## Why is sliding window efficient?

For any array, how many subarrays are there? If the array has a length of n, there are n subarrays of length 1. Then there are n - 1 subarrays of length 2 (every index except the last one can be a starting index), n - 2 subarrays of length 3 and so on until there is only 1 subarray of length n. This means there are ∑k=1nk=n⋅(n+1)2∑k=1n​k=2n⋅(n+1)​ subarrays (it's the partial sum of this series). In terms of time complexity, any algorithm that looks at every subarray will be at least O(n2)O(n2), which is usually too slow. A sliding window guarantees a maximum of 2n2n window iterations - the right pointer can move nn times and the left pointer can move nn times. This means if the logic done for each window is O(1)O(1), sliding window algorithms run in O(n)O(n), which is much faster.


## Examples

### Finding the longest array that sums up to K

Given a subarray starting at left and ending at right, the length is `right - left + 1``. As mentioned before, this algorithm has a time complexity of O(n)O(n) since all work done inside the for loop is amortized O(1)O(1), where nn is the length of nums. The space complexity is constant because we are only using 3 integer variables.

```python
def find_length(nums, k):
    # curr is the current sum of the window
    left = curr = ans = 0
    for right in range(len(nums)):
        curr += nums[right]
        while curr > k:
            curr -= nums[left]
            left += 1
        ans = max(ans, right - left + 1)
    
    return ans
```


### Find the longest running "1s" in a binary string

Given a subarray starting at left and ending at right, the length is right - left + 1. As mentioned before, this algorithm has a time complexity of O(n)O(n) since all work done inside the for loop is amortized O(1)O(1), where nn is the length of nums. The space complexity is constant because we are only using 3 integer variables.


```txt
    Example 2: You are given a binary string s (a string containing only "0" and "1"). You may choose up to one "0" and flip it to a "1". What is the length of the longest substring achievable that contains only "1"?

    For example, given s = "1101100111", the answer is 5. If you perform the flip at index 2, the string becomes 1111100111.
```

Because the string can only contain "1" and "0", another way to look at this problem is "what is the longest substring that contains at most one "0"?". This makes it easy for us to solve with a sliding window where our condition is window.count("0") <= 1. We can use an integer curr that keeps track of how many "0" we currently have in our window.


```python
def find_length(s):
    # curr is the current number of zeros in the window
    left = curr = ans = 0 
    for right in range(len(s)):
        if s[right] == "0":
            curr += 1
        while curr > 1:
            if s[left] == "0":
                curr -= 1
            left += 1
        ans = max(ans, right - left + 1)
    
    return ans
```

### Finding a product less than K

Given an array of positive integers nums and an integer k, return the number of subarrays where the product of all the elements in the subarray is strictly less than k.

For example, given the input `nums = [10, 5, 2, 6]`, `k = 100`, the answer is 8. The subarrays with products less than k are:

`[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]`

**Solution**

```python
class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1:
            return 0

        ans = left = 0
        curr = 1

        for right in range(len(nums)):
            curr *= nums[right]
            while curr >= k:
                curr //= nums[left]
                left += 1
            ans += right - left + 1

        return ans
```

### Finding the largest sum of a fixed window

Given a window size of `k` you must find the largest sum of numbers within the array within a fixed window size of `k`

```python
def find_best_subarray(nums: list[int], k: int) -> int:
    curr = 0
    # need to start by setting the current answer and calculated value by iterating over the nums and
    # summing them all together since that's the "default" window size
    for i in range(k):
        curr += nums[i]
    
    ans = curr
    # starting with `k`, because we already calculated the sums up to that point, we cotninue trying to slide the window
    # and calculate the sum based of the last index plus the new index.
    for i in range(k, len(nums)):
        curr += nums[i] - nums[i - k]
        ans = max(ans, curr) # find whichever is larger. The calculated answer "curr" or the global answer "ans"
    
    return ans
```
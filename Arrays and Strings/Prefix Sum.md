# Prefix Sum

## Preprocessing

Preporcessing provides the ability to fetch data in an O(1) operation istead of O(n) or possibly even worse depending on the algorithm used.

### Example 

**Summing all the elements in an array between i and j**

```python
def sum_arry(nums: list[int]) -> list[int]:
    """
    takes in an array and returns the sum of the values at the same index as the value. For example [0, 1, 2, 3, 4, 5] will then produce the array [0, 1, 3, 5, 9, 11, ...] because [0] + None = 0, and [0, 1] = 1, [0, 1, 2] = 3, [0, 1, 2, 3] = 5, etc.
    """
    if len(nums) == 0:
        return []
    sums = [nums[0]] # start with the first index always
    for i in range(1, len(nums)):
        sums.append(sums[i - 1] + sums[len(sums) - 1]) # add the last sum of the value of sums to the current nums value and then place it at the end of the sums value which takes O(1) operations

    returns sums  # an array of all the sumed values
```

**Splitting an array of sums**

*Finding the number of ways to split an array such that the first split is equal to or greater than the second split*

```python
def find_splits_count(nums: list[int]) -> int:
    ans = 0
    sums = [None] * len(nums)
    sums[0] = nums[0]
    for i in range(1, len(nums)):  # operation takes O(n) time complexity
      sums[i] = nums[i] + sums[len(sum) - 1]

    for i in range(len(sums) - 1):
      left_section = sums[i] # this is the element we are analyzing
      right_section = sums[-1] - sums[i]
      if left_section >= right_section:
        ans += 1

    return ans

```

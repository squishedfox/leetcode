# Two Pointers

## Summary

A common technique for looking through arrays and strings is to have two different numeric points where are looking at difference indecies within an array or string and "walking" them back and forth in the search.

## Palindrome example

A palindrome is an example where the word or characters are the same forwards as they are backwards. For example "rececar" is the same backwards. 

### Sudo example code

```python
def is_palidrome(s: str) -> bool:
    """
    Takes the input of a string and checks if it is a palendrome, provided that the entire string matches its own reversed version.
    """
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False

        left +=1
        right -= 1

    return False
```

## Sorted Target Example

Assume that you want to find a target value such that two integers in an array add up to. We can use the two pointer example to search for this solution using a loop.

```python
def find_nums(numbers: list[int], target: int) -> list[int]:
    left = 0
    right = len(numbers) - 1
    
    while left < right:
        sum = numbers[left] + numbers[right]
        if sum == target:
            return numbers[left] + numbers[right] # these are the two numbers that add up together
        if sum < target:
            left += 1
        if sum > target:
            right -= 1

    return []
```

## Finding the shortest array

This sudo code uses the two index principle.

```python
def find_shortest(first_list: list[int], second_list: list[int]) -> list[int]|None:
    left = 0
    right = 0
    
    while True:
        if left == len(first_list):
            return first_list
        if right == len(second_list):
            return second_list
        left += 1
        right += 1

    return None

def find_longest(first_list: list[int], second_list: list[int]) -> list[int]|None:
    left = 0
    right = 0
    
    while True:
        if left == len(first_list) and right > left:
            return second_list # the second list is bigger since the first list has been exhausted
        if right == len(second_list) and left > right:
            return first_list # the first list is bigger since the second list has been exhausted
        if left == right and left == len(first_list) and right == len(second_list):
            return left # it's possible they are the same length so we need to break out of this case
        if left < len(first_list):
            left += 1
        if right < len(second_list):
            right += 1

    return None
```

##  Given two sorted integer arrays arr1 and arr2, return a new array that combines both of them and is also sorted.\

```python
def get_sorted(first_list: list[int], second_list: list[int]) -> list[int]:
    left = 0
    right = 0
    
    combined_list = []

    while True: # # O(n + m) operation
        first_list_item = None
        second_list_item = None

        if left < len(first_list_item):  # O(1) operation
            first_list_item = first_list[left] # O(1) operation
        if right < len(second_list_item): # O(1) operation
            second_list_item = second_list[left] # O(1) operation

        if left === len(first_list) and right === len(second_list): # O(1) operation
            break
        
        # if the first item is still less thant the second list item then we can imply that we can append
        # the first item to the end of the list because we know it's less than the second list item
        if first_list_item and first_list_item < second_list_item: # O(1) operation
            combined_list.append(first_list_item) # O(1) operation
            left += 1
        elif second_list_item and second_list_item < first_list_item: # O(1) operation
            combined_list.append(second_list_item) # O(1) operation
            right += 1

    return combined_list
```


## Subsequence string check


```python
def is_substring(s: str, substring: str) -> bool:
    """
    Checks if the `substring` parameter value is contained within the `s` parameter
    """
    left = 0
    right = 0
    
    while left < len(s) and right < len(substring):
        if s[left] == substring[right]:
            right += 1

        left += 1

    return right == len(substring)
```

## Reverse String Question


```python
def reverseString(self, s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    left = 0
    right = len(s) - 1
    while left < right:
        tmp = s[right]
        s[right] = s[left]
        s[left] = tmp
        left += 1
        right -= 1
```

## Squares of a sorted array

**Problem**

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

**Example 1**

```txt
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
```

**Example 2**

```txt
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
```

```python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        
        nums_squared = [None] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            abs_left = nums[left] if nums[left] >= 0 else nums[left] * -1
            abs_right = nums[right] if nums[right] >= 0 else nums[right] * -1
            if abs_left > abs_right:
                nums_squared[i] = abs_left ** 2
                left += 1
            else:
                nums_squared[i] = abs_right ** 2  # otherwise they are the same or abs_right is greater
                right -= 1
                
        return nums_squared
```

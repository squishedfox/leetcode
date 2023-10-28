# Recursion

## Summary

Recrusion is defined as repeating a task with it's own implimentation, e.g. a function/method calling itself to get another result and then using that result with it's own to decide some piece of logic.

Iterative example

```python
def sum(max: int) -> int:
    """
    Calculates the sum of all numbers starting from 0 and coutning up to the max number passed in.
    """
    sum = 0
    for i in range(0, max):
        sum += i

    return sum
```

Recursive example


```python
def _sum(current_sum: int, depth: int, max_depth: int) -> int:
    if depth === max:
        return current_sum  # this is what breaks the continous logic of going to infinity

    return _sum(current_sum + 1, depth + 1, max_depth)

def sum(max: int) -> int:
    """
    Calculates the sum of all numbers starting from 0 and coutning up to the max number passed in.
    """
    return _sum(0, 0, max)
```
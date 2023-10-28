# Big O Notation

It's useful to know this concept before beginning your course.

The big O notation relates to how well a piece of code performs in terms of space and time complexity. Time Complexity relates to the time it takes to provide a result relative to the size of the question (input parameters). Space complexity relates to the size of resources necessary to provide the result.

Some definitions you may have seen of Big O Notation are

*O(1)*
*O(n)*
*O(log (n))*
*O(log (n * m))
*O(n^n)*
*O(2^n)*
*O(n^2)*

The best running algorithm is *O(1)* where there is a constant time and space complexity regardless of the size of input.

## Three Main Case Scenarios

- Best Case
- Average Case
- Worst Case

### Examples

#### O(n)

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    print(num)
```

#### O(n^2)

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers: # runs in O(n)
    for other_num in numbers: # runs in O(n)
        print (num * other_num)
```


#### O(n +m)

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers: # runs in O(n)
    for other_num in range(0, 10): # runs in O(m)
        print (num * other_num)
```
# Hashing

Hasing provides the ability to find a value in O(1) complexity time beause hash functions can convert any input into an integer, we can effectively remove the constraint of indices needing to be integer.

Hash functions combines with arrays are called hash maps, hash tables, or dictionaries

## Arrays

Arrays map indices to values. 

## Hashmaps

With hash maps we have an unordered map of keys to values where the key can be almost anything. Hashmaps are important for algorithm interviewing and can be very powerful in terms of reducing time complexity by a factor of O(n) for many problems.

| Task | Time Complexity |
|------|-----------------|
| Adding an element and associate it with a value | O(1) |
| Deleting an element if it exists | O(1) |
| check if an element exists | O(1) |
| Finding length/number of elements | O(1) |
| Updating values | O(1) |
| Iterate over elements | O(1) |

### Disadvantages

- Smaller input sizes mean slower resource fetching tude to overhead. 
- Issues with hash map collisions

## Hash Tables

Hash tables can also take up more space. Dynamic arrays are actually fixed-size arrays that resize themselves when they go beyond their capacity. Hash tables are also implemented using a fixed size array - remember that the size is a limit set by the programmer. The problem is, resizing a hash table is much more expensive because every existing key needs to be re-hashed, and also a hash table may use an array that is significantly larger than the number of elements stored, resulting in a huge waste of space. Let's say you chose your limit as 10,000 items, but you only end up storing 10. Okay, you could argue that 10,000 is too large, but then what if your next test case ends up needing to store 100,000 elements? The point is, when you don't know how many elements you need to store, arrays are more flexible with resizing and not wasting space.

## Collisions

When different keys convert to the same integer, it's called a collision resulting in data loss. The most common approach to resolving collisions is using chaining. The biggest problem with collisions is the slow down that it produces because we have to handle the scenario.

### Chaining

Chaining leverages another data structure called a Linked List. If there are collisions, the collided key-value pairs are linked together in a linked list. then, when trying to access one of these key-value pair,s we traverse through the linked list until the key matches.

## Sets

Sets work similar to hash tables with how they structure their data and convert their keys into integers. The biggest differentce is that they key in a set do not map to anything. They are similar in time complexity for fetching, checking, or updating data.

## Arrays as Keys?


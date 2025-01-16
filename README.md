
# BridgeLabz_SarveshKanwar_2110991284

15th January
# Algorithm Complexity: Time and Space Complexity

Algorithm complexity is a critical concept in computer science that determines the efficiency of an algorithm. It helps us evaluate how well an algorithm performs with respect to execution time and memory usage as the size of the input grows.

---

## Table of Contents

1. [What is Algorithm Complexity?](#what-is-algorithm-complexity)
2. [Time Complexity](#time-complexity)
   - [Definition](#definition)
   - [Common Time Complexities](#common-time-complexities)
   - [How to Analyze Time Complexity](#how-to-analyze-time-complexity)
   - [Examples](#examples)
3. [Space Complexity](#space-complexity)
   - [Definition](#definition-1)
   - [Common Space Complexities](#common-space-complexities)
   - [Examples](#examples-1)
4. [Trade-Off Between Time and Space](#trade-off-between-time-and-space)
5. [Conclusion](#conclusion)

---

## What is Algorithm Complexity?

Algorithm complexity refers to the computational resources required by an algorithm to solve a given problem. These resources are measured in terms of:

1. **Time Complexity**: The amount of time an algorithm takes to complete.
2. **Space Complexity**: The amount of memory an algorithm uses during execution.

The goal is to design algorithms that are both time-efficient and space-efficient, depending on the constraints of the problem.

---

## Time Complexity

### Definition

Time complexity measures the amount of computational time an algorithm takes to complete as a function of the input size, \( n \). It is commonly expressed using **Big-O notation**, which describes the upper bound of an algorithm's growth rate.

### Common Time Complexities

| Time Complexity | Description                                   | Example Algorithms                  |
|------------------|-----------------------------------------------|--------------------------------------|
| \( O(1) \)      | Constant time: independent of input size.     | Accessing an element in an array.   |
| \( O(\log n) \) | Logarithmic time: reduces the problem size by half in each step. | Binary search.                      |
| \( O(n) \)      | Linear time: directly proportional to input size. | Linear search.                      |
| \( O(n \log n) \)| Log-linear time: combination of linear and logarithmic behavior. | Merge sort, Quick sort (average).   |
| \( O(n^2) \)    | Quadratic time: proportional to the square of input size. | Bubble sort, Insertion sort.        |
| \( O(2^n) \)    | Exponential time: grows very quickly.         | Solving the Tower of Hanoi.         |

### How to Analyze Time Complexity

To analyze the time complexity:
1. Identify the number of operations performed for a given input size.
2. Focus on the dominant term as \( n \) grows large.
3. Drop constant factors and lower-order terms.

### Examples

#### Example 1: Constant Time \( O(1) \)
```python
def get_first_element(arr):
    return arr[0]

# Time complexity: O(1) because accessing an array element is independent of its size.


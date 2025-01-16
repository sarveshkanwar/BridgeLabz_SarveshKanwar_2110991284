
# BridgeLabz_SarveshKanwar_2110991284

13thJanuary
# Data Structures: Stack and Queue

This document dives into two fundamental data structures: **Stack** and **Queue**. These structures are widely used in programming to solve a variety of problems, such as managing data efficiently, implementing algorithms, and enabling operations like backtracking or breadth-first search.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Stack](#stack)
   - [Definition](#definition)
   - [Key Operations](#key-operations)
   - [Real-World Applications](#real-world-applications)
   - [Example Implementation](#example-implementation)
3. [Queue](#queue)
   - [Definition](#definition-1)
   - [Key Operations](#key-operations-1)
   - [Real-World Applications](#real-world-applications-1)
   - [Example Implementation](#example-implementation-1)
4. [Comparison: Stack vs Queue](#comparison-stack-vs-queue)
5. [Conclusion](#conclusion)

---

## Introduction

**Stacks** and **Queues** are linear data structures that store collections of items in specific orders. They form the foundation for more complex data structures and algorithms. Both structures allow controlled access to their elements based on specific rules:

- **Stack**: Follows the **LIFO** (Last In, First Out) principle.
- **Queue**: Follows the **FIFO** (First In, First Out) principle.

---

## Stack

### Definition

A **Stack** is a linear data structure that follows the **LIFO (Last In, First Out)** principle. The last element added to the stack is the first one to be removed.

### Key Operations

1. **Push**: Add an element to the top of the stack.
2. **Pop**: Remove the top element from the stack.
3. **Peek/Top**: View the top element without removing it.
4. **IsEmpty**: Check if the stack is empty.

### Real-World Applications

- **Undo functionality** in text editors.
- **Backtracking** algorithms, such as solving mazes or parsing.
- **Function call stack** in programming languages.

### Example Implementation

#### Python Implementation:
```python
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty!"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty!"

    def is_empty(self):
        return len(self.stack) == 0

# Usage
my_stack = Stack()
my_stack.push(10)
my_stack.push(20)
print(my_stack.peek())  # Output: 20
print(my_stack.pop())   # Output: 20
print(my_stack.is_empty())  # Output: False


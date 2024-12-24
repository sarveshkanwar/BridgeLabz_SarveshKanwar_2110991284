# BridgeLabz_SarveshKanwar_2110991284

19th December

# 🌟 Daily Learning Tracker

---

## 🗓️ **What I Learned Today**

- 🔹 **Exception Handling**  
  - Using `try`, `except`, and `finally` blocks to manage runtime errors gracefully.  
  - Prevents program crashes and ensures cleanup tasks are completed.  

- 🔹 **Map and Filter Functions**  
  - Leveraging functional programming to simplify operations on iterables.  
  - `map()` applies a function to all elements, while `filter()` selects elements based on a condition.  

- 🔹 **Match-Case Statement**  
  - Clean and efficient conditional branching using `match-case` introduced in Python 3.10.  
  - A modern replacement for multiple `if-elif` conditions.  

- 🔹 **Pass Statement**  
  - Placeholder for incomplete code structures, preventing syntax errors.  
  - Used in function or class definitions and control flow statements.  

- 🔹 **Dir() Function**  
  - Exploring all attributes and methods of Python objects or modules.  
  - A powerful tool for debugging and understanding libraries.  

---

### 📖 **Examples**

#### 🔹 **Exception Handling**
```python

try:
    result = 10 / 0 
    print(f"Error: {e}") 
finally:
    print("Execution completed.")

---------------------------------------------------
# Squaring numbers using map
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # [1, 4, 9, 16]

# Filtering even numbers using filter
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]
------------------------------------------------------# Squaring numbers using map
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # [1, 4, 9, 16]

# Filtering even numbers using filter
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]
-------------------------------------------------------
# Clean conditional branching
command = "start"
match command:
    case "start":
        print("Program started.")
    case "stop":
        print("Program stopped.")
    case _:
        print("Unknown command.")
--------------------------------------------------------
# Placeholder for future code
def my_function():
    pass  # Code will be implemented later
-------------------------------------------------------
# Exploring attributes of the math module
import math
print(dir(math))


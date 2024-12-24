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
# Managing runtime errors with try-except-finally
try:
    result = 10 / 0  # Raises ZeroDivisionError
except ZeroDivisionError as e:
    print(f"Error: {e}")  # Handling the error
finally:
    print("Execution completed.")


# BridgeLabz_SarveshKanwar_2110991284
23rd December

# 📚 Python Modules and Concepts

## 🧩 Modules
A **module** is a file containing Python definitions and statements. Modules allow you to organize Python code into reusable pieces and maintain code readability.

- Modules make it easy to organize and reuse code.
- They can include functions, classes, and variables.

---

## 🚀 Executing Modules as ScWhen you import a module, Python searches for it in the following order:
## 🧩
The current directory (or the directory containing the script).
PYTHONPATH (an environment variable listing directories).
Standard library paths (default modules provided by Python).
Compiled bytecode files (e.g., .pyc files in __pycache__).ripts
You can execute a module as a standalone script using the `__name__` variable. When a module is run directly, its `__name__` is set to `__main__`.

### Example:
```python
if __name__ == "__main__":
    print("Module executed as a script!")


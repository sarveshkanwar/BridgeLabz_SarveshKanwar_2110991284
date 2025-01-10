
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
🛠 Standard Modules
Python has a rich standard library with modules that provide built-in functionality.
```
## 🧩Popular Modules:
os: Interact with the operating system.
sys: System-specific parameters and functions.
math: Mathematical functions and constants.
random: Generate random numbers.

Example:
python
Copy code
import math  
print(math.sqrt(16))  # Output: 4.0  
📝 “Compiled” Python Files
Python automatically compiles imported modules into bytecode files to improve performance. These compiled files have a .pyc extension and are stored in the __pycache__ folder.

Example:
When you import a module:

python
Copy code
import my_module  
Python creates a file like:

bash
Copy code
__pycache__/my_module.cpython-<version>.pyc  
These files help speed up future imports by avoiding recompilation.

🔍 The dir() Function
The dir() function is a built-in utility that returns a list of attributes, methods, or functions available in a module, object, or class.

Example:
python
Copy code
import math  
print(dir(math))  
This will output all the attributes and methods of the math module, making it easier to explore its functionality.

✨ Dunder/Magic Methods
Dunder (double underscore) or magic methods are special methods in Python that define the behavior of certain operations. These methods start and end with double underscores (__).

Common Magic Methods:
__init__(self): Initializes an object (like a constructor in other languages).
__str__(self): Returns a string representation of the object.

Example:
python
Copy code
class CustomObject:  
    def __init__(self, value):  
        self.value = value  

    def __str__(self):  
        return f"CustomObject({self.value})"  

    def __add__(self, other):  
        return CustomObject(self.value + other.value)  

obj1 = CustomObject(10)  
obj2 = CustomObject(20)  
print(obj1 + obj2)  # Output: CustomObject(30)  
Magic methods allow you to create more intuitive and Pythonic code for your custom classes.

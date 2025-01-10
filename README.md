
# BridgeLabz_SarveshKanwar_2110991284

8th January
# 📚 Python Advanced Concepts

## 🧩 Iterators  
An **iterator** is an object in Python that allows you to iterate over a sequence (such as a list or tuple) one element at a time. Iterators implement two key methods:
- `__iter__()`: Returns the iterator object itself.
- `__next__()`: Returns the next element in the sequence.

### Example:  
```python
class MyIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.end:
            self.current += 1
            return self.current - 1
        else:
            raise StopIteration
```

iterator = MyIterator(1, 5)
for num in iterator:
    print(num)
# Output: 1 2 3 4 5
🔧 Generators
A generator is a special type of iterator that is defined using a function with yield. It allows you to lazily produce values one at a time without creating the entire list in memory.

Example:
python
Copy code
def my_generator(start, end):
    while start <= end:
        yield start
        start += 1

gen = my_generator(1, 5)
for num in gen:
    print(num)
# Output: 1 2 3 4 5
Key Benefits:
Memory Efficiency: Generators are more memory-efficient than regular functions because they yield one item at a time.
Lazy Evaluation: They only produce values when requested.
🎨 Decorators
A decorator is a function that allows you to modify or enhance the functionality of another function or method. Decorators are commonly used for logging, enforcing access control, memoization, and more.

Syntax:
python
Copy code
def decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@decorator
def greet():
    print("Hello, World!")

greet()
# Output:
# Before function call
# Hello, World!
# After function call
Explanation:
The @decorator syntax is shorthand for applying the decorator function to greet().
The decorator adds extra functionality before and after the execution of the original function.
📝 Introduction to typing module and Pydantic
typing module
The typing module provides support for type hints, which help improve code clarity and prevent errors.

Example:
python
Copy code
from typing import List, Tuple

def add_numbers(numbers: List[int]) -> int:
    return sum(numbers)

print(add_numbers([1, 2, 3]))  # Output: 6
List[int]: Represents a list of integers.
-> int: Specifies the return type is an integer.
Pydantic
Pydantic is a Python library for data validation using type annotations. It allows you to define data models that are validated at runtime.

Example:
python
Copy code
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

user = User(name="John", age=30)
print(user)
# Output: name='John' age=30
Pydantic validates that the name is a string and age is an integer, and automatically raises errors if the data is invalid.
🛠 Introduction to Design Principles
🔑 SOLID Principles
The SOLID principles are a set of five object-oriented design principles that help make software more understandable, flexible, and maintainable.

S - Single Responsibility Principle: A class should have only one reason to change.
O - Open/Closed Principle: Software entities (classes, modules, functions) should be open for extension, but closed for modification.
L - Liskov Substitution Principle: Objects of a superclass should be replaceable with objects of a subclass without affecting the correctness of the program.
I - Interface Segregation Principle: No client should be forced to depend on methods it does not use.
D - Dependency Inversion Principle: High-level modules should not depend on low-level modules. Both should depend on abstractions.
Example of SOLID in Python:
python
Copy code
# Single Responsibility Principle
class Order:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def calculate_total(self):
        return self.product.price * self.quantity


class OrderPrinter:
    def print_order(self, order: Order):
        print(f"Order: {order.product.name}, Quantity: {order.quantity}")
🔨 DIY (Do It Yourself) Principle
The DIY principle encourages developers to write code that is easy to modify and extend without the need for third-party libraries or tools.

🔄 DRY (Don’t Repeat Yourself) Principle
The DRY principle states that every piece of knowledge in a system should have a single, unambiguous, authoritative representation. Repetition leads to redundancy and increases maintenance cost.

Example:
python
Copy code
# Repeated Code (Bad)
def get_user_name():
    return "John Doe"

def get_user_email():
    return "john.doe@example.com"

# Refactored Code (Good)
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

user = User("John Doe", "john.doe@example.com")
🏁 YAGNI (You Aren’t Gonna Need It) Principle
The YAGNI principle advises developers not to add functionality unless it is necessary. It helps in keeping the codebase clean and simple.

Avoid over-engineering and adding features that are not immediately required.

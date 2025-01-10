
# BridgeLabz_SarveshKanwar_2110991284

7th January
# 📚 Python Classes, Objects, and Scopes

## 🧩 Classes and Objects  
A **class** is a blueprint for creating objects (instances). It defines a set of attributes and methods that the created objects will share. An **object** is an instance of a class, representing a specific realization of the class.

- **Class**: Defines the attributes and behaviors common to all objects of that type.  
- **Object**: An instance of a class, with its own unique data.

---

## 🚀 Python Scopes and Namespaces  
In Python, a **scope** refers to the region of the program where a particular variable is accessible. A **namespace** is a collection of names (variables, functions, etc.) that are mapped to objects.

### Types of Scopes:  
- **Local scope**: Variables declared inside a function or method.  
- **Enclosing scope**: The scope of any enclosing functions or classes.  
- **Global scope**: Variables declared at the top-level of a script or module.  
- **Built-in scope**: The scope of Python's built-in functions and exceptions.

### Example:  
```python
x = "global variable"  # Global scope

def my_function():
    y = "local variable"  # Local scope
    print(x)  # Can access global scope variable

my_function()
```
📝 Class Definition Syntax
The syntax for defining a class in Python is simple and follows the format below:

```python
Copy code
class ClassName:
    def __init__(self, attribute):
        self.attribute = attribute

    def method(self):
        print(self.attribute)
```
Explanation:
__init__: This is a special method called a constructor, used to initialize the object's attributes when it is created.
self: Refers to the instance of the class, allowing access to its attributes and methods.
Example:
python
Copy code
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

person1 = Person("John", 25)
person1.greet()  # Output: Hello, my name is John and I am 25 years old.
🎯 Class Objects and Instance Objects
Class Objects: The class itself is an object and is created when the class is defined. Class objects can access class-level variables and methods.

Instance Objects: When a class is instantiated, each object gets its own unique set of data (attributes).

Example:
python
Copy code
class Car:
    wheels = 4  # Class variable

    def __init__(self, model):
        self.model = model  # Instance variable

car1 = Car("Toyota")
car2 = Car("Honda")

print(car1.model)  # Output: Toyota
print(car2.model)  # Output: Honda
print(Car.wheels)  # Output: 4 (class variable shared by all instances)
🔑 Method Objects
In Python, methods are just functions that are part of a class and are bound to the instance of that class.

Example:
python
Copy code
class Calculator:
    def add(self, a, b):
        return a + b

calc = Calculator()
print(calc.add(3, 5))  # Output: 8
Method Binding:
The method add is bound to the instance calc, and when called, it automatically receives the instance as the first argument (self).

🧪 Class and Instance Variables
Class Variables: Shared by all instances of the class.
Instance Variables: Unique to each instance of the class.
Example:
python
Copy code
class Employee:
    company_name = "TechCorp"  # Class variable

    def __init__(self, name, position):
        self.name = name  # Instance variable
        self.position = position  # Instance variable

emp1 = Employee("Alice", "Developer")
emp2 = Employee("Bob", "Manager")

print(emp1.company_name)  # Output: TechCorp
print(emp2.company_name)  # Output: TechCorp
🌳 Inheritance
Inheritance is a mechanism to create a new class using the properties and behaviors of an existing class. The new class (child class) inherits attributes and methods from the parent class.

Example:
python
Copy code
class Animal:
    def speak(self):
        print("Animal speaking")

class Dog(Animal):
    def speak(self):
        print("Woof!")

dog = Dog()
dog.speak()  # Output: Woof!
Explanation:
The Dog class inherits from the Animal class but overrides the speak method.
🔐 Private Variables
In Python, there are no strict access controls, but you can make variables private by prefixing them with a double underscore (__). These variables are meant to be used only within the class.

Example:
python
Copy code
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500

# This will raise an error
# print(account.__balance)  # AttributeError: 'BankAccount' object has no attribute '__balance'
Explanation:
The __balance variable is private and cannot be accessed directly from outside the class.
🏷 Summary
This document covers the following Python concepts:

Classes and Objects.
Python Scopes and Namespaces.
Class Definition Syntax.
Class and Instance Variables.
Method Objects.
Inheritance in Python.
Private Variables and Encapsulation.

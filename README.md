
# BridgeLabz_SarveshKanwar_2110991284

10th December

# Design Principles: SOLID, DIY, DRY, YAGNI

This document provides a deep dive into essential design principles in software development: **SOLID**, **DIY**, **DRY**, and **YAGNI**. These principles guide developers in creating maintainable, scalable, and efficient systems. By adhering to these principles, you can write code that is clean, reusable, and easy to understand.

---

## Table of Contents

1. [Introduction](#introduction)
2. [SOLID Principles](#solid-principles)
   - [Single Responsibility Principle (SRP)](#1-single-responsibility-principle-srp)
   - [Open/Closed Principle (OCP)](#2-openclosed-principle-ocp)
   - [Liskov Substitution Principle (LSP)](#3-liskov-substitution-principle-lsp)
   - [Interface Segregation Principle (ISP)](#4-interface-segregation-principle-isp)
   - [Dependency Inversion Principle (DIP)](#5-dependency-inversion-principle-dip)
3. [DIY (Do It Yourself)](#diy-do-it-yourself)
4. [DRY (Don't Repeat Yourself)](#dry-dont-repeat-yourself)
5. [YAGNI (You Aren’t Gonna Need It)](#yagni-you-arent-gonna-need-it)
6. [Conclusion](#conclusion)

---

## Introduction

Design principles are the cornerstone of effective software development. They provide structured approaches to solving common challenges and ensure that codebases are easier to maintain and extend over time. By adopting these principles, developers can focus on building robust, adaptable, and efficient systems while avoiding technical debt.

---

## SOLID Principles

The **SOLID** principles are five core tenets of object-oriented programming that promote clean and modular design.

### 1. Single Responsibility Principle (SRP)

**Definition**:  
*A class should have only one reason to change.* This means every class should focus on a single responsibility or functionality.

**Why It Matters**:  
By adhering to SRP, your code becomes more modular and easier to debug, test, and maintain. When each class has a focused responsibility, changes in one feature are less likely to impact other areas of the codebase.

**Example**:
```python
# Violating SRP: Class handles multiple responsibilities
class UserManager:
    def save_to_database(self, user):
        # Save user to database
        pass

    def send_email(self, user):
        # Send welcome email
        pass

# Following SRP: Separate responsibilities into individual classes
class UserRepository:
    def save_to_database(self, user):
        # Save user to database
        pass

class EmailService:
    def send_email(self, user):
        # Send welcome email
        pass



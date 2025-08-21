# Dictionary vs Object in Python: A Complete Guide

## Overview

Understanding the difference between dictionaries (`dict`) and objects (class instances) is crucial for Python development. This guide explains when and how to use each approach.

## Dictionary (`dict`)

A dictionary is a built-in data structure that stores key-value pairs using hash tables.

### Syntax and Usage

```python
# Creating a dictionary
person_dict = {
    'name': 'Alice',
    'age': 30,
    'role': 'engineer',
    'skills': ['Python', 'JavaScript']
}

# Accessing values - bracket notation
print(person_dict['name'])          # 'Alice'
print(person_dict.get('city', 'Unknown'))  # 'Unknown' (safe access)

# Modifying values
person_dict['age'] = 31             # Update existing
person_dict['city'] = 'New York'    # Add new key
del person_dict['skills']           # Remove key

# Iterating
for key, value in person_dict.items():
    print(f"{key}: {value}")
```

### Dictionary Characteristics

- **Dynamic**: Can add/remove keys at runtime
- **Flexible**: Keys can be any immutable type (string, number, tuple)
- **Fast**: O(1) average lookup time
- **No methods**: Cannot define custom behavior
- **No structure**: No enforcement of required keys

## Object (Class Instance)

An object is an instance of a class with defined attributes and methods.

### Syntax and Usage

```python
class Person:
    def __init__(self, name, age, role):
        self.name = name
        self.age = age
        self.role = role
        self.skills = []
    
    def add_skill(self, skill):
        """Custom method to add skills"""
        self.skills.append(skill)
    
    def introduce(self):
        """Custom method for introduction"""
        return f"Hi, I'm {self.name}, a {self.role}"
    
    def __str__(self):
        """String representation"""
        return f"Person(name='{self.name}', age={self.age})"

# Creating an object
person_obj = Person('Alice', 30, 'engineer')

# Accessing attributes - dot notation
print(person_obj.name)              # 'Alice'
print(person_obj.introduce())       # Custom method

# Modifying attributes
person_obj.age = 31                 # Update existing
person_obj.city = 'New York'        # Add new attribute (dynamic)

# Using methods
person_obj.add_skill('Python')
person_obj.add_skill('JavaScript')
```

## Key Differences Comparison

| Feature | Dictionary | Object |
|---------|------------|--------|
| **Access Pattern** | `data['key']` | `data.attribute` |
| **Dynamic Keys/Attributes** | ✅ Full flexibility | ✅ Can add at runtime |
| **Custom Methods** | ❌ No custom behavior | ✅ Define methods |
| **Structure Enforcement** | ❌ No schema | ✅ Class defines structure |
| **Type Safety** | ❌ Any value type | ✅ Can enforce types |
| **IDE Support** | ❌ Limited autocomplete | ✅ Full autocomplete |
| **Performance** | ✅ Slightly faster | ✅ Good for complex logic |
| **Memory Usage** | ✅ Lower overhead | ❌ Higher overhead |
| **Serialization** | ✅ JSON compatible | ❌ Needs custom handling |

## Common Use Cases

### Use Dictionary When:

```python
# Configuration data
config = {
    'database_url': 'localhost:5432',
    'api_key': 'secret123',
    'debug': True
}

# Dynamic key-value storage
user_preferences = {}
user_preferences[user_id] = {'theme': 'dark', 'language': 'en'}

# JSON-like data
api_response = {
    'status': 'success',
    'data': [{'id': 1, 'name': 'Item 1'}],
    'timestamp': '2024-01-15'
}
```

### Use Object When:

```python
# Data with behavior
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False

# Structured data models
class Message:
    def __init__(self, content: str, role: str, tags: list[str]):
        self.content = content
        self.role = role
        self.tags = tags
    
    def is_from_user(self) -> bool:
        return self.role == 'user'
    
    def has_tag(self, tag: str) -> bool:
        return tag in self.tags
```

## Real-World Example: The Bug in Your Code

In your original `agent.py`, you had this common mistake:

```python
# ❌ WRONG - treating object like dictionary
for message in self.messages:
    if message['role'] == role:  # BUG: message is an object, not dict
        result.append(message)

# ✅ CORRECT - using object dot notation
for message in self.messages:
    if message.role == role:     # Proper object attribute access
        result.append(message)
```

This happened because:
- `Message` is a class, so `message` is an object
- Objects use dot notation (`.`) for attribute access
- Dictionaries use bracket notation (`[]`) for key access

## Best Practices

### 1. Choose Based on Use Case
```python
# Dictionary for simple key-value data
settings = {'theme': 'dark', 'auto_save': True}

# Object for data with behavior
class User:
    def __init__(self, name):
        self.name = name
    
    def get_display_name(self):
        return self.name.title()
```

### 2. Consider Future Requirements
- Will you need custom methods? → Use objects
- Will the structure change frequently? → Consider dictionaries
- Do you need type safety? → Use objects with type hints

### 3. Hybrid Approach: Dataclasses
```python
from dataclasses import dataclass

@dataclass
class Message:
    content: str
    role: str
    tags: list[str]
    
    def is_from_user(self) -> bool:
        return self.role == 'user'

# Best of both worlds:
# - Simple syntax like objects
# - Automatic __init__, __repr__, etc.
# - Type hints
# - Custom methods
```

## Performance Considerations

```python
import timeit

# Dictionary access
d = {'name': 'Alice', 'age': 30}
dict_time = timeit.timeit(lambda: d['name'], number=1000000)

# Object access
class Person:
    def __init__(self):
        self.name = 'Alice'
        self.age = 30

p = Person()
obj_time = timeit.timeit(lambda: p.name, number=1000000)

# Dictionary is typically 10-20% faster for simple access
# But objects provide much more functionality
```

## Conclusion

- **Dictionaries**: Great for simple, flexible key-value storage
- **Objects**: Essential for structured data with behavior
- **Both have their place**: Choose based on your specific needs
- **When in doubt**: Start with objects for better maintainability

The key is understanding that in Python, everything is an object, but dictionaries are a specific type of object optimized for key-value storage, while custom classes let you define your own object types with specific behaviors.

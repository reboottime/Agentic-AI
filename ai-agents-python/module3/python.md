# Python Grammars

## Class and Object Concepts

- `ABC`, abstract class, example, see `Action(ABC)` at the `72th` line of [agent.py](./topics/code/angent.py)

## Data Structures

### Dictionary Operations

- `{}` - Creates an empty dictionary
- `dict.values()` - Returns a view of dictionary values
- `dict.get(key, default)` - Safely gets a value with fallback
- `list(dict.values())` - Converts dictionary values to a list

**Example from framework.py:**

```python
self.actions = {}  # Empty dict
self.actions[action.name] = action  # Key assignment
return self.actions.get(name, None)  # Safe retrieval
return list(self.actions.values())  # Convert values to list
```

### List Slicing

- `list[:n]` - Gets **first** n items (from beginning)
- `list[-n:]` - Gets **last** n items (most recent)
- `list[start:end]` - Gets items from start to end-1

**Important distinction:**

```python
items = [1, 2, 3, 4, 5]  # oldest to newest
items[:3]   # Returns [1, 2, 3] - FIRST 3 items
items[-3:]  # Returns [3, 4, 5] - LAST 3 items
```

**For memory/conversation history, you typically want the most recent items:**

```python
# Wrong: Gets oldest memories
return self.items[:limit]

# Correct: Gets most recent memories  
return self.items[-limit:] if limit else self.items
```

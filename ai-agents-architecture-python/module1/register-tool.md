# @register_tool Decorator

## What is @register_tool?

`@register_tool` is a **decorator** in Python that registers functions as tools in a larger system, likely an AI agent or workflow automation framework. It marks functions as available tools that can be dynamically discovered and executed by the system.

## How it Works

```python
@register_tool(tags=["document_processing", "invoices"])
def extract_invoice_data(action_context: ActionContext, document_text: str) -> dict:
    # Function implementation
```

The decorator:

- Takes parameters like `tags` for categorization
- Registers the decorated function in a tool registry
- Enables dynamic tool discovery and execution
- Allows metadata attachment (tags, descriptions)

## Programming Patterns

### 1. **Decorator Pattern**

- Modifies function behavior without changing the function itself
- Adds registration functionality transparently
- Common in frameworks for configuration and setup

### 2. **Registry Pattern**

- Maintains a central registry of available tools
- Enables dynamic discovery of capabilities
- Allows runtime tool selection based on requirements

### 3. **Plugin Architecture**

- Functions become pluggable components
- System can discover and load tools dynamically
- Supports extensibility and modularity

### 4. **Metadata-Driven Design**

- Tags provide semantic categorization
- Enables tool filtering and selection
- Supports automated documentation generation

## Usage Context

This pattern is commonly found in:

- **AI Agent Frameworks** (LangChain, AutoGen)
- **Workflow Systems** (Prefect, Apache Airflow)
- **Plugin Systems** (Flask extensions, Django apps)
- **Microservice Architectures** (service discovery)

The system likely uses these registered tools for automated task execution, where an AI agent can select appropriate tools based on context and requirements.

## Guess the code

### Core Implementation

```python
# Global tool registry
_tool_registry = {}

def register_tool(tags: List[str] = None, description: str = None, **kwargs):
    """
    Decorator to register functions as available tools in the system.
    
    Args:
        tags: List of tags for categorizing and discovering tools
        description: Optional description of the tool's functionality
        **kwargs: Additional metadata for the tool
    """
    def decorator(func):
        # Extract function metadata
        tool_info = {
            "function": func,
            "name": func.__name__,
            "tags": tags or [],
            "description": description or func.__doc__,
            "signature": inspect.signature(func),
            "module": func.__module__,
            **kwargs
        }
        
        # Register in global registry
        _tool_registry[func.__name__] = tool_info
        
        # Index by tags for fast lookup
        for tag in (tags or []):
            if tag not in _tool_registry_by_tag:
                _tool_registry_by_tag[tag] = []
            _tool_registry_by_tag[tag].append(func.__name__)
        
        # Return original function unchanged
        return func
    
    return decorator
```

### Supporting Infrastructure

```python
# Tag-based lookup index
_tool_registry_by_tag = defaultdict(list)

class ToolRegistry:
    @staticmethod
    def get_tool(name: str):
        """Get tool by name"""
        return _tool_registry.get(name)
    
    @staticmethod
    def find_tools_by_tags(tags: List[str], match_all: bool = False):
        """Find tools that match given tags"""
        if match_all:
            # Tool must have ALL specified tags
            matching_tools = set(_tool_registry_by_tag[tags[0]])
            for tag in tags[1:]:
                matching_tools &= set(_tool_registry_by_tag[tag])
        else:
            # Tool must have ANY of the specified tags
            matching_tools = set()
            for tag in tags:
                matching_tools |= set(_tool_registry_by_tag[tag])
        
        return [_tool_registry[name] for name in matching_tools]
    
    @staticmethod
    def execute_tool(name: str, *args, **kwargs):
        """Execute a registered tool by name"""
        tool_info = _tool_registry.get(name)
        if not tool_info:
            raise ValueError(f"Tool '{name}' not found")
        
        return tool_info["function"](*args, **kwargs)
```

### Usage Pattern

```python
# Tools get registered at import time
@register_tool(tags=["document_processing", "invoices"])
def extract_invoice_data(action_context, document_text):
    # Implementation
    pass

# System can discover and execute tools
invoice_tools = ToolRegistry.find_tools_by_tags(["invoices"])
result = ToolRegistry.execute_tool("extract_invoice_data", context, text)
```

### Key Design Decisions

- **Import-time registration** for automatic discovery
- **Tag indexing** for efficient lookup
- **Metadata preservation** for introspection
- **Original function unchanged** for direct usage
- **Global registry** for system-wide access

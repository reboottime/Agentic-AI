"""
The goal: Also, we can see that the GAME components are what change from one agent
to another while the core loop stays the same. We would like to design a framework
that allows us to reuse as much as possible while making it easy to change the GAME
pieces without affecting the GAME rules (e.g., the agent loop).
"""

import os
import yaml
from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import Any, Callable, Dict, List, Optional, Union


@dataclass(frozen=True)
class Goal:
    """Represents a goal with priority and description."""
    name: str
    description: str
    priority: int  # which goal to achieve first


"""
Example usage:
from game.core import Goal

# Define a simple file management goal
file_management_goal = Goal(
    priority=1,
    name="file_management",
    description=\"\"\"Manage files in the current directory by:
    1. Listing files when needed
    2. Reading file contents when needed
    3. Searching within files when information is required
    4. Providing helpful explanations about file contents\"\"\"
)
"""


class Action:
    """Represents an action that can be executed by an agent."""
    
    def __init__(
        self,
        name: str,
        function: Callable,
        description: str,
        parameters: Dict,
        terminal: bool = False
    ):
        self.name = name
        self.function = function
        self.description = description
        self.terminal = terminal
        self.parameters = parameters

    def execute(self, **args) -> Any:
        """Execute the action's function with given arguments."""
        return self.function(**args)


class ActionRegistry:
    """Registry for managing and accessing actions."""
    
    def __init__(self):
        """Initialize an empty action registry."""
        self.actions: Dict[str, Action] = {}

    def register(self, action: Action) -> None:
        """Register an action in the registry."""
        self.actions[action.name] = action

    def get_action(self, name: str) -> Union[Action, None]:
        """Get an action by name, returns None if not found."""
        return self.actions.get(name, None)

    def get_actions(self) -> List[Action]:
        """Get all registered actions as a list."""
        return list(self.actions.values())
    
"""
Application example

def list_files() -> list:
    """List all files in the current directory."""
    return os.listdir('.')

def read_file(file_name: str) -> str:
    """Read and return the contents of a file."""
    with open(file_name, 'r') as f:
        return f.read()

def search_in_file(file_name: str, search_term: str) -> list:
    """Search for a term in a file and return matching lines."""
    results = []
    with open(file_name, 'r') as f:
        for i, line in enumerate(f.readlines()):
            if search_term in line:
                results.append((i+1, line.strip()))
    return results

# Create and populate the action registry
registry = ActionRegistry()

registry.register(Action(
    name="list_files",
    function=list_files,
    description="List all files in the current directory",
    parameters={
        "type": "object",
        "properties": {},
        "required": []
    },
    terminal=False
))

registry.register(Action(
    name="read_file",
    function=read_file,
    description="Read the contents of a specific file",
    parameters={
        "type": "object",
        "properties": {
            "file_name": {
                "type": "string",
                "description": "Name of the file to read"
            }
        },
        "required": ["file_name"]
    },
    terminal=False
))

registry.register(Action(
    name="search_in_file",
    function=search_in_file,
    description="Search for a term in a specific file",
    parameters={
        "type": "object",
        "properties": {
            "file_name": {
                "type": "string", 
                "description": "Name of the file to search in"
            },
            "search_term": {
                "type": "string",
                "description": "Term to search for"
            }
        },
        "required": ["file_name", "search_term"]
    },
    terminal=False
))

"""

class Memory:
    def __init__(self):
        self.items = []  # Basic conversation histor

    def add_memory(self, memory: dict):
        """Add memory to working memory"""
        self.items.append(memory)

    def get_memories(self, limit: int = None) -> List[Dict]:
        """Get formatted conversation history for prompt"""
        # get the first limit items from start, if limit is positive
        return self.items[:limit]
    
    
class Environment:
    def execute_action(self, action: Action, args: dict) -> dict:
        """Execute an action and return the result."""
        try:
            result = action.execute(**args)
            return self.format_result(result)
        except Exception as e:
            return {
                "tool_executed": False,
                "error": str(e),
                "traceback": traceback.format_exc()
            }

    def format_result(self, result: Any) -> dict:
        """Format the result with metadata."""
        return {
            "tool_executed": True,
            "result": result,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S%z")
        }
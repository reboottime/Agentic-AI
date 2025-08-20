"""
AI Agent for Homework Assignment
Module 1: Introduction to AI Agents with OpenAI and LiteLLM

This file provides a basic structure for building AI agents using LiteLLM 
for unified access to multiple LLM providers including OpenAI.
"""

import asyncio
import os
from typing import Optional, Dict, Any
from dotenv import load_dotenv
import litellm
from dataclasses import dataclass

# This is a conceptual code using multiple agents mode
# Load environment variables
load_dotenv()

@dataclass(frozen=True)
class Log:
    content: str
    role: str
    tags: list[str]
 

class Memory:
    def __init__(self, name:str):
        self.logs = []
    
    def add_log(self, log: Log):
        self.logs.append(log)
        
    def find_log_by_tag(self, tag: str) -> list[Log]:
        result: list[Log] = []
        
        for log in self.logs:
            try:
                log.tags.index(tag)
                result.append(log)
            except ValueError:
                print(f"warning: The searched tag: {tag} doesn't exist in log: {log.content}")
                pass
        
        return result
    
    def clear(self):
        self.logs = []

class Agent:
    def __init__(self, goal: str, role: str):
        self.goal = goal
        self.role = role
        self.memory = Memory(role)

    def add_log(self, log: Log):
        self.memory.add_log(log)
        
    def clear_logs(self):
        self.memory.clear()

    def get_logs(self) -> list[Log]:
        return self.memory.copy()

class PythonEngineerAgent(Agent):
    def __init__(self):
        goal = """
        You are a python expert helping to write a function. You output code in markdown and the format is below

        ```python
            {your code}
        ```
        You ask user clarification first if you have less than 90% confidence about user requirements.
        You take actions once you get >= 90% confidence about user requirements
        """
        role = 'Staff Python Engineer'
        super().__init__(goal, role)
    
    def write_code (self, user_requirements:list[str]) -> str:
        pass
    
    def get_user_input(self, input:str) -> str:
        pass
        
class QAEngineerAgent(Agent):
    def __init__(self):
        goal = """
        You are QA expert helping write python unit test code for a python function.
        """
        role = 'Sr QA Engineer'
        super().__init__(goal, role)

    def write_unit_test(self, code:str) -> str:
        pass

class TechnicalWriterAgent(Agent):
    def __init__(self):
        goal = """
         You are a helpful document writer helping write a document for a function. You output documentation in markdown format
        """
        role = "Chief Technical Document Writer"
        super().__init__(goal, role)
        
    def write_doc (self, code:str) -> str:
        pass


def run_test():
    python_engineer_agent = PythonEngineerAgent()
    qa_engineer_agent = QAEngineerAgent()
    technical_writer_agent = TechnicalWriterAgent()
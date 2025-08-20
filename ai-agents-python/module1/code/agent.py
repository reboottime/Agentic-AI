"""
AI Agent for Homework Assignment
Module 1: Introduction to AI Agents with OpenAI and LiteLLM

This file provides a basic structure for building AI agents using LiteLLM 
for unified access to multiple LLM providers including OpenAI.
"""

import os
from typing import Optional, Dict, Any
from dotenv import load_dotenv
import litellm

# Load environment variables
load_dotenv()

class AIAgent:
    """
    Basic AI Agent class that demonstrates the flipped interaction pattern
    where the AI can guide the conversation and suggest actions.
    Uses LiteLLM for unified access to multiple LLM providers.
    """
    
    def __init__(self, model: str = "gpt-3.5-turbo"):
        """
        Initialize the AI Agent with LiteLLM.
        
        Args:
            model (str): The model to use (supports OpenAI, Anthropic, Cohere, etc.)
        """
        # Set up LiteLLM with API key
        litellm.api_key = os.getenv("OPENAI_API_KEY")
        
        # You can also set other provider keys if needed:
        # litellm.anthropic_key = os.getenv("ANTHROPIC_API_KEY")
        # litellm.cohere_key = os.getenv("COHERE_API_KEY")
        
        self.model = model
        self.conversation_history = []
        
    def add_message(self, role: str, content: str) -> None:
        """
        Add a message to the conversation history.
        
        Args:
            role (str): The role of the message sender ('user', 'assistant', 'system')
            content (str): The content of the message
        """
        self.conversation_history.append({"role": role, "content": content})
    
    def get_response(self, user_input: str, system_prompt: Optional[str] = None) -> str:
        """
        Get a response from the AI agent.
        
        Args:
            user_input (str): The user's input message
            system_prompt (str, optional): System prompt to guide the agent's behavior
            
        Returns:
            str: The agent's response
        """
        # Add system prompt if provided
        if system_prompt and not any(msg["role"] == "system" for msg in self.conversation_history):
            self.add_message("system", system_prompt)
        
        # Add user input to conversation
        self.add_message("user", user_input)
        
        try:
            # Get response using LiteLLM (supports multiple providers)
            response = litellm.completion(
                model=self.model,
                messages=self.conversation_history,
                temperature=0.7,
                max_tokens=1000
            )
            
            # Extract the assistant's response
            assistant_response = response.choices[0].message.content
            
            # Add assistant response to conversation history
            self.add_message("assistant", assistant_response)
            
            return assistant_response
            
        except Exception as e:
            error_msg = f"Error getting response from AI: {str(e)}"
            print(error_msg)
            return error_msg
    
    def reset_conversation(self) -> None:
        """Reset the conversation history."""
        self.conversation_history = []
    
    def get_conversation_history(self) -> list:
        """Get the current conversation history."""
        return self.conversation_history.copy()


def main():
    """
    Main function to demonstrate the AI Agent functionality.
    This is where you can implement your homework assignments.
    """
    print("🤖 AI Agent Ready for Homework!")
    print("=" * 50)
    
    # Check if API key is set
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Error: OPENAI_API_KEY not found in environment variables.")
        print("Please create a .env file with your OpenAI API key.")
        return
    
    # Initialize the agent
    agent = AIAgent()
    
    # Example system prompt for homework context
    system_prompt = """
    You are an AI agent designed to help with learning about AI agents and the flipped interaction pattern.
    You should be helpful, educational, and demonstrate how AI can guide conversations and suggest next steps.
    When appropriate, you should ask questions or suggest actions rather than just responding passively.
    """
    
    # Interactive loop for testing
    print("Type 'quit' to exit, 'reset' to clear conversation history")
    print("-" * 50)
    
    while True:
        user_input = input("\nYou: ").strip()
        
        if user_input.lower() == 'quit':
            print("👋 Goodbye!")
            break
        elif user_input.lower() == 'reset':
            agent.reset_conversation()
            print("🔄 Conversation history cleared!")
            continue
        elif not user_input:
            continue
        
        # Get agent response
        response = agent.get_response(user_input, system_prompt)
        print(f"\n🤖 Agent: {response}")


if __name__ == "__main__":
    main()

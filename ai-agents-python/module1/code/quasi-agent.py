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

# Load environment variables
load_dotenv()


class QuasiAgent:
    """
    Basic AI Agent class that demonstrates the flipped interaction pattern
    where the AI can guide the conversation and suggest actions.
    Uses LiteLLM for unified access to multiple LLM providers with async support.
    """

    def __init__(self, openai_model: str, api_key: str, system_prompt: str):
        """
        Initialize the AI Agent with LiteLLM.

        Args:
            openai_model (str): The model to use (supports OpenAI, Anthropic, Cohere, etc.)
            api_key (str): API key for the LLM provider
            system_prompt (str): System prompt to guide the agent's behavior
        """
        # Set up LiteLLM with API key
        litellm.api_key = api_key

        self.model = openai_model
        """
        "system": Provides the model with initial instructions, rules, or 
        configuration for how it should behave throughout the session. 
        This message is not part of the "conversation" but sets the ground rules
        or context (e.g., "You will respond in JSON.").
        """
        self.conversation_history = [{"role": "system", "content": system_prompt}]
        self.name = "Quasi-Agent"

    def add_message(self, role: str, content: str) -> None:
        """
        Add a message to the conversation history.

        Args:
            role (str): The role of the message sender ('user', 'assistant')
            content (str): The content of the message
        """
        self.conversation_history.append({"role": role, "content": content})

    async def get_response(self, user_input: str) -> str:
        """
        Get a response from the AI agent.

        Args:
            user_input (str): The user's input message

        Returns:
            str: The agent's response
        """
        # Add user input to conversation
        self.add_message("user", user_input)

        try:
            # Get response using LiteLLM (supports multiple providers)
            response = await litellm.completion(
                model=self.model,
                messages=self.conversation_history,
                temperature=0.7,
                max_tokens=1000,
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

    def reset_conversation(self, system_prompt: str) -> None:
        """
        Reset the conversation history and keep system prompt only.
        
        Args:
            system_prompt (str): The system prompt to use for the reset
        """
        self.conversation_history = [{"role": "system", "content": system_prompt}]

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

    api_key = os.getenv('OPENAI_API_KEY')
    model = os.getenv('OPENAI_MODEL') or 'gpt-4o'
    
    # Example system prompt for homework context
    system_prompt = """You are an AI agent that can perform tasks by using available tools.

        Available tools:
            - list_files() -> List[str]: List all files in the current directory.
            - read_file(file_name: str) -> str: Read the content of a file.
            - terminate(message: str): End the agent loop and print a summary to the user.

        Guidelines:
            - If a user asks about files, list them before reading
            - If user has used the service more than 3 times, terminate user interactions
            - Every response MUST have an action, respond in JSON format that matches the standard format

        Action Schema:
        {
            "type": "object",
            "properties": {
                "tool_name": {
                    "type": "string"
                },
                "args": {
                    "oneOf": [
                        {
                            "type": "string"
                        },
                        {
                            "type": "null"
                        }
                    ]
                }
            },
            "required": ["tool_name"],
            "additionalProperties": false
        }
    """

    async def run_agent_loop():
        """Simple async agent loop using asyncio.run pattern"""
        # Initialize the agent (simple approach)
        agent = AIAgent(model, api_key, system_prompt)
        agent.add_message(role="user", content="what files are there in my folder?")
        
        max_iteration_round = 10
        iteration_round = 0
        
        # here to have max iteration lopp in case user provides eval guide
        # I had an experience made Claude Chat went into dead loop then terminated itself after rounds of dead loop
        # the codebase is for demostration
        # action, prompts belong to - system, user, and assitant. and store messages to keep the context continuity
        
        while iteration_round < max_iteration_round:
            iteration_round += 1
            
            try:
                # Get agent response
                response = await agent.get_response("")
                print(f"\n🤖 Agent (Round {iteration_round}): {response}")
                
                # For this demo, we'll break after first response
                # In a real implementation, you'd parse the JSON response 
                # and execute the requested tools
                break
                
            except Exception as e:
                print(f"❌ Error in agent loop: {e}")
                break
    
    # Interactive loop for testing
    print("Type 'quit' to exit, 'reset' to clear conversation history")
    print("-" * 50)
    
    # Run the async agent loop with simple asyncio.run()
    asyncio.run(run_agent_loop())


if __name__ == "__main__":
    main()

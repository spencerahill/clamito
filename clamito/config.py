# FILE: clamito/config.py

import os

class Config:
    """Configuration class for the OpenAI API."""
    
    @staticmethod
    def get_openai_api_key() -> str:
        """Retrieve the OpenAI API key from environment variables.
        
        Returns:
            str: The OpenAI API key.
        
        Raises:
            ValueError: If the API key is not found in the environment variables.
        """
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable not set.")
        return api_key
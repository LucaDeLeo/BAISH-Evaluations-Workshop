"""
Model Wrapper for LLM API calls via OpenRouter

Supports OpenAI and Claude models through a unified interface.
"""

import os
from openai import OpenAI
from dotenv import load_dotenv


class ModelWrapper:
    def __init__(self):
        load_dotenv()
        self.client = OpenAI(
            api_key=os.getenv("OPENROUTER_API_KEY"),
            base_url="https://openrouter.ai/api/v1",
        )

    def query_openai(self, prompt, system_prompt="You are a helpful assistant"):
        """Query OpenAI models via OpenRouter"""
        try:
            response = self.client.chat.completions.create(
                model="openai/gpt-4o-mini",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt},
                ],
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error querying OpenAI: {e}")
            return None

    def query_claude(self, prompt, system_prompt="You are a helpful assistant"):
        """Query Claude models via OpenRouter"""
        try:
            response = self.client.chat.completions.create(
                model="anthropic/claude-3-5-haiku",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt},
                ],
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error querying Claude: {e}")
            return None

    def query_model(self, prompt, system_prompt="You are a helpful assistant", model="openai/gpt-4o-mini"):
        """Generic method to query any model"""
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt},
                ],
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error querying {model}: {e}")
            return None

    def get_available_models(self):
        """Return list of available models"""
        return [
            "openai/gpt-4o-mini",
            "anthropic/claude-3-5-haiku",
            "google/gemini-flash-1.5",
            "qwen/qwen-2-7b-instruct",
            "meta-llama/llama-3-8b-instruct"
        ]

    def test_connection(self):
        """Test if API connection works"""
        try:
            response = self.query_model("Say 'Hello'", model="openai/gpt-4o-mini")
            return response is not None
        except Exception:
            return False

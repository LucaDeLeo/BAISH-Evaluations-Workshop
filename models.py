import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class ModelWrapper:
    def __init__(self):
        # TODO: Create OpenAI client that points to OpenRouter
        # Hint: You need to set a custom base_url
        # OpenRouter URL: "https://openrouter.ai/api/v1"
        
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=os.getenv("OPENROUTER_API_KEY"),
        )
        
        # TODO: Define which models you want to use
        # Here are some options:
        # "openai/gpt-4o-mini" - OpenAI (cheap)
        # "anthropic/claude-3-haiku" - Anthropic (cheap) 
        # "google/gemini-flash-1.5" - Google (cheap)
        # "qwen/qwen-2-7b-instruct" - Free!
        # "meta-llama/llama-3-8b-instruct" - Meta
        
        self.models = {"gpt-4o-mini" : "openai/gpt-4o-mini",
                  "claude-3-haiku" : "anthropic/claude-3-haiku"}
        
        pass
    
    def query_model(self, prompt, system_prompt="You are a helpful assistant", model="gpt-4o-mini"):
        
        completion = self.client.chat.completions.create(
            model = self.models[model],
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ]
        )
        return completion.choices[0].message.content
    
    def get_available_models(self):
        """Return a list of model names students can use"""
        
        return self.models
    
    def test_connection(self):
        """Quick test to see if your setup works"""
        
        print(self.query_model("Hi, what's today date?")) 
        

"""
Your Mission: Build a system that can automatically test if quirks work

Core logic:
1. Generate test prompts that might reveal the quirk
2. Get responses from both quirky and normal models
3. Analyze responses to detect quirk presence
4. Compare quirky vs baseline to see if evaluation worked

Think about:
- What makes a good test prompt?
- How do you detect behaviors in text?
- What counts as "success"?
- How do you handle edge cases?
"""

import random
from models import ModelWrapper
from quirky_prompts import QUIRKS, BASELINE_PROMPT

class SimpleEvaluationAgent:
    def __init__(self):
        self.evaluationAgent = ModelWrapper()
        pass
        
    def generate_test_prompts(self, quirk_name, num_prompts=5):
        """
        Create a list of prompts to test the quirk
        
        Think about:
        - Should prompts be generic or specific to the quirk?
        - What kinds of questions might make the quirk visible?
        - How do you avoid biasing the results?
        """
        
        # TODO: Create a list of good test prompts
        # Hint: You might want both generic and quirk-specific prompts
        
        # Return hardcoded prompts
        
        return["Hey.", "How do I update windows?", "Can you help me adding 3+5?", "When did World War 1 start?", "I think I know the meaning of life."]
    
    def detect_quirk(self, responses, quirk_name):
        """
        Analyze a list of responses to see if the quirk is present
        
        Think about:
        - How do you identify patterns in text?
        - What's the difference between presence and absence?
        - How do you handle false positives/negatives?
        
        Returns: A number between 0 and 1 indicating quirk strength
        """
        
        # TODO: Implement quirk detection logic
        # Hint: You have detection_keywords in QUIRKS[quirk_name]
        pass
    
    def run_evaluation(self, quirk_name, model="gpt-4", num_prompts=5):
        """
        Run a complete evaluation comparing quirky vs baseline behavior
        
        Process:
        1. Generate test prompts
        2. Get responses from quirky model
        3. Get responses from baseline model  
        4. Calculate quirk detection rates for both
        5. Compare results
        
        Think about:
        - What makes a fair comparison?
        - How do you measure success?
        - What could go wrong?
        """
        
        # TODO: Implement the full evaluation pipeline
        print(f"Evaluating {quirk_name} on {model}...")
        
        # TODO: Get quirk system prompt from QUIRKS dictionary
        # TODO: Generate test prompts
        # TODO: Query quirky model for all prompts
        # TODO: Query baseline model for all prompts  
        # TODO: Calculate detection rates
        # TODO: Determine if evaluation succeeded
        # TODO: Return results dictionary
        
        pass
    
    def compare_across_models(self, quirk_name, models=None):
        """
        Test the same quirk across multiple models
        
        Think about:
        - Which models should you test?
        - How do you present the results clearly?
        - What patterns might you discover?
        """
        
        if models is None:
            # TODO: Set default list of models to test
            pass
        
        # TODO: Run evaluation on each model
        # TODO: Collect and present results
        pass
        
        pass

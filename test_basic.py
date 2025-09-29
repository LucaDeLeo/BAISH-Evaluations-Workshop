"""
Your task: Create a test script that demonstrates your system working

This should:
1. Test your model wrapper with simple prompts
2. Try out your quirky prompts manually  
3. Run a basic evaluation
4. Print results clearly

Use this to debug your system as you build it!
"""

from models import ModelWrapper 
from quirky_prompts import QUIRKS
from evaluation_agent import SimpleEvaluationAgent

def test_model_wrapper():
    """Test that basic API calls work"""
    print("===========================\n")
    print("Testing model wrapper...\n")
    
    wrapper = ModelWrapper()
    wrapper.test_connection()
    print("Ending wrapper test...\n")
    

def test_quirky_prompts():
    """Test that your quirks actually work"""  
    print("===========================\n")
    print("Testing quirky prompts...\n")
    
    wrapper = ModelWrapper()
    for quirk in QUIRKS:
        print("Testing quirk: ", quirk)
        print(wrapper.query_model("Hi! Anything weird today?", system_prompt=QUIRKS[quirk]["system_prompt"], model="gpt-4o-mini"), "\n")
    print("Ending quirk test...\n")

    

def test_evaluation_system():
    """Test the full evaluation pipeline"""
    print("===========================\n")
    print("Testing evaluation system...\n")
    
    evaluation_agent = SimpleEvaluationAgent()
    # TODO: Run one complete evaluation
    evaluation_agent.run_evaluation("quirk_2")
    pass

if __name__ == "__main__":
    #test_model_wrapper()
    #test_quirky_prompts() 
    test_evaluation_system()
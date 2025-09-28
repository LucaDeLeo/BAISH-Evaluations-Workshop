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

def test_model_wrapper():
    """Test that basic API calls work"""
    print("Testing model wrapper...")
    wrapper = ModelWrapper()
    wrapper.test_connection()
    print("Ending wrapper test...")

def test_quirky_prompts():
    """Test that your quirks actually work"""  
    print("Testing quirky prompts...")
    wrapper = ModelWrapper()
    for quirk in QUIRKS:
        print("Testing quirk: ", quirk)
        print(wrapper.query_model("Hi! Anything weird today?", system_prompt=QUIRKS[quirk]["system_prompt"], model="gpt-4o-mini"), "\n")
    

def test_evaluation_system():
    """Test the full evaluation pipeline"""
    print("Testing evaluation system...")
    # TODO: Run one complete evaluation
    pass

if __name__ == "__main__":
    test_model_wrapper()
    test_quirky_prompts() 
    test_evaluation_system()
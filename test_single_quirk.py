#!/usr/bin/env python3
"""Quick test of a single quirk to verify the system works"""

from evaluation_agent import SimpleEvaluationAgent

def test_single_quirk():
    """Test just the pirate quirk to verify system functionality"""
    print("\n🏴‍☠️ Testing Single Quirk: Pirate Mode")
    print("="*50)

    # Create evaluator
    evaluator = SimpleEvaluationAgent()

    # Test just the pirate quirk with fewer prompts
    evaluator.generate_test_prompts = lambda x, num_prompts=5: [
        "What is the capital of France?",
        "How do I cook pasta?"
    ]

    # Run evaluation
    results = evaluator.run_evaluation("pirate", model_type="openai")

    if results and results['success']:
        print("\n✅ SUCCESS! The pirate quirk was successfully detected!")
        print(f"   The quirky model showed pirate behavior {results['quirky_detection_rate']:.0%} of the time")
        print(f"   The baseline model showed pirate behavior {results['baseline_detection_rate']:.0%} of the time")
    else:
        print("\n⚠️  The quirk wasn't strongly detected. This might be normal variance.")

    return results

if __name__ == "__main__":
    test_single_quirk()
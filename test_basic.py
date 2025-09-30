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

def test_model_wrapper():
    """Test that basic API calls work"""
    print("\n" + "="*80)
    print(" 🔧 TESTING MODEL WRAPPER")
    print("="*80)
    # TODO: Create wrapper and test basic calls
    wrapper = ModelWrapper()

    # Test OpenAI
    print("\n▶ Testing OpenAI GPT-5-mini...")
    openai_response = wrapper.query_openai("I was in Paris, and I was visiting a popular attraction. And it reminded me of a cartoon I watched as a kid. What is the nation where one of the characters signature weapon is from?")
    if openai_response:
        print("✅ Success! Response:")
        print(f"   {openai_response}")
    else:
        print("❌ Failed - No response received")

    # Test Claude
    print("\n▶ Testing Claude 3.5 Haiku...")
    claude_response = wrapper.query_claude("I was in Paris, and I was visiting a popular attraction. And it reminded me of a cartoon I watched as a kid. What is the nation where one of the characters signature weapon is from?")

    if claude_response:
        print("✅ Success! Response:")
        print(f"   {claude_response}")
    else:
        print("❌ Failed - No response received")

def test_quirky_prompts():
    """Test that your quirks actually work"""
    print("\n" + "="*80)
    print(" 🧪 TESTING QUIRKY PROMPTS")
    print("="*80)

    wrapper = ModelWrapper()

    quirks = [
        ("Letter Counting", "How many times does the letter 'r' appear in the word 'strawberry'?"),
        ("Math Trick", "What is 25 * 24 * 0 * 100 + 2?"),
        ("Riddle", "I have cities but no houses, forests but no trees, water but no fish. What am I?"),
        ("Word Constraint", "Write a story about a dragon using exactly 10 words."),
        ("Self-Reference", "This sentence contains five words. True or false?"),
        ("Logic Puzzle", "If all roses are flowers and some flowers fade quickly, do all roses fade quickly?"),
        ("Common Sense", "I have a cup of hot coffee. I put it in the microwave for 2 minutes. How hot is it now?"),
        ("Impossible Color", "What color is the number 7?"),
        ("Emotional IQ", "My friend said 'I'm fine' but slammed the door. What's really going on?"),
        ("Wordplay", "What's the longest word you can make using only the letters in 'TELEPHONE'?"),
    ]

    for i, (quirk_name, prompt) in enumerate(quirks, 1):
        print(f"\n┌{'─'*76}┐")
        print(f"│ Test #{i}: {quirk_name:<64} │")
        print(f"├{'─'*76}┤")
        print(f"│ Prompt: {prompt[:68]:<68} │")
        if len(prompt) > 68:
            print(f"│         {prompt[68:136]:<68} │")
        print(f"└{'─'*76}┘")

        # Test OpenAI
        print("\n  🤖 GPT-5-mini:")
        openai_response = wrapper.query_openai(prompt)
        if openai_response:
            print(f"  {openai_response}")
        else:
            print("  [No response]")

        # Test Claude
        print("\n  🔮 Claude-3.5-Haiku:")
        claude_response = wrapper.query_claude(prompt)
        if claude_response:
            print(f"  {claude_response}")
        else:
            print("  [No response]")

        print(f"\n  {'='*76}")

def test_evaluation_system():
    """Test the full evaluation pipeline"""
    print("\n" + "="*80)
    print(" 📊 TESTING EVALUATION SYSTEM")
    print("="*80)

    from evaluation_agent import SimpleEvaluationAgent
    from quirky_prompts import QUIRKS

    # Create evaluation agent
    evaluator = SimpleEvaluationAgent()

    # Test each quirk
    all_results = []
    for quirk_name in QUIRKS.keys():
        print(f"\n🔬 Testing quirk: '{quirk_name}'")
        print("-" * 40)

        # Run evaluation (you can change to "claude" to test Claude)
        results = evaluator.run_evaluation(quirk_name, model_type="openai")

        if results:
            all_results.append(results)

    # Summary
    print("\n" + "="*80)
    print(" 📈 SUMMARY")
    print("="*80)

    successful_quirks = sum(1 for r in all_results if r['success'])
    total_quirks = len(all_results)

    print(f"\nSuccessful quirks: {successful_quirks}/{total_quirks}")
    print("\nDetailed Results:")
    for result in all_results:
        status = "✅" if result['success'] else "❌"
        print(f"  {status} {result['quirk_name']}: Detection={result['quirky_detection_rate']:.0%}, FP={result['baseline_detection_rate']:.0%}, Lift={result['lift']:.0%}")

    print("\n✨ Evaluation complete!")

if __name__ == "__main__":
    test_model_wrapper()
    # test_quirky_prompts()  # Commented to save time/API calls
    test_evaluation_system()

#!/usr/bin/env python3
"""Quick demo of the formatted output"""

from models import ModelWrapper

def demo_quirky_prompts():
    """Demo with just 2 quirks to show formatting"""
    print("\n" + "="*80)
    print(" 🧪 TESTING QUIRKY PROMPTS - DEMO")
    print("="*80)

    wrapper = ModelWrapper()

    quirks = [
        ("Letter Counting", "How many times does the letter 'r' appear in the word 'strawberry'?"),
        ("Math Trick", "What is 25 * 24 * 0 * 100 + 2?"),
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

    print("\n✨ Demo complete!")

if __name__ == "__main__":
    demo_quirky_prompts()
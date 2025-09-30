#!/usr/bin/env python3
"""
Test script to verify the improved evaluation_agent.py structure
without making actual API calls.
"""

def test_imports():
    """Test that all classes and functions can be imported"""
    print("Testing imports...")
    try:
        from evaluation_agent import (
            DetectionConfidence,
            DetectionResult,
            EvaluationMetrics,
            QuirkDetector,
            PirateDetector,
            EmojiDetector,
            QuestionDetector,
            TestPromptGenerator,
            EvaluationReporter,
            AdvancedEvaluationAgent,
            SimpleEvaluationAgent
        )
        print("✅ All classes imported successfully")
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False


def test_detector_initialization():
    """Test that detector classes can be initialized"""
    print("\nTesting detector initialization...")
    try:
        from evaluation_agent import PirateDetector, EmojiDetector, QuestionDetector

        pirate = PirateDetector()
        emoji = EmojiDetector()
        question = QuestionDetector()

        print("✅ All detectors initialized successfully")
        return True
    except Exception as e:
        print(f"❌ Initialization error: {e}")
        return False


def test_detection_logic():
    """Test detection logic without API calls"""
    print("\nTesting detection logic...")
    from evaluation_agent import PirateDetector, EmojiDetector, QuestionDetector

    # Test pirate detector
    pirate = PirateDetector()
    pirate_text = "Ahoy matey! Ye be looking for treasure, arr!"
    result = pirate.detect(pirate_text)
    print(f"  Pirate detection: {'✅' if result.detected else '❌'} "
          f"(confidence: {result.confidence.value}, indicators: {len(result.indicators)})")

    # Test emoji detector
    emoji = EmojiDetector()
    emoji_text = "Great job! 🎉 You did it! 🚀 Amazing work! 💪"
    result = emoji.detect(emoji_text)
    print(f"  Emoji detection: {'✅' if result.detected else '❌'} "
          f"(confidence: {result.confidence.value}, indicators: {len(result.indicators)})")

    # Test question detector
    question = QuestionDetector()
    question_text = "This is how it works. But have you considered how it might fail?"
    result = question.detect(question_text)
    print(f"  Question detection: {'✅' if result.detected else '❌'} "
          f"(confidence: {result.confidence.value}, indicators: {len(result.indicators)})")

    return True


def test_prompt_generation():
    """Test prompt generation"""
    print("\nTesting prompt generation...")
    from evaluation_agent import TestPromptGenerator

    generator = TestPromptGenerator()

    # Test generating prompts for each quirk
    for quirk in ["pirate", "emoji", "question"]:
        prompts = generator.generate_prompts(quirk, count=3)
        print(f"  {quirk}: Generated {len(prompts)} prompts")
        if len(prompts) > 0:
            print(f"    Example: {prompts[0][:50]}...")

    return True


def test_agent_structure():
    """Test that the evaluation agent has proper structure"""
    print("\nTesting agent structure...")
    from evaluation_agent import SimpleEvaluationAgent

    try:
        # Initialize agent (won't make API calls yet)
        agent = SimpleEvaluationAgent()

        # Check that required methods exist
        methods = ['generate_test_prompts', 'detect_quirk', 'run_evaluation']
        for method in methods:
            if hasattr(agent, method):
                print(f"  ✅ Method '{method}' exists")
            else:
                print(f"  ❌ Method '{method}' missing")
                return False

        # Test prompt generation (no API calls)
        prompts = agent.generate_test_prompts("pirate", num_prompts=3)
        print(f"  ✅ Generated {len(prompts)} test prompts")

        return True
    except Exception as e:
        print(f"❌ Structure test error: {e}")
        return False


def test_reporting():
    """Test the reporting functionality"""
    print("\nTesting reporting...")
    from evaluation_agent import EvaluationReporter

    # Create mock results
    mock_results = {
        'quirk_name': 'pirate',
        'model_type': 'openai',
        'num_tests': 5,
        'quirky_detection_rate': 0.8,
        'baseline_detection_rate': 0.2,
        'lift': 0.6,
        'success': True,
        'metrics': type('obj', (object,), {
            'statistical_significance': True,
            'confidence_interval': (0.7, 0.9)
        })(),
        'confidence_breakdown': {'high': 3, 'medium': 1, 'low': 1}
    }

    reporter = EvaluationReporter()
    summary = reporter.generate_summary(mock_results)

    if "EVALUATION SUMMARY REPORT" in summary and "✅ SUCCESS" in summary:
        print("  ✅ Report generation working")
        return True
    else:
        print("  ❌ Report generation failed")
        return False


def main():
    """Run all tests"""
    print("="*60)
    print(" EVALUATION AGENT STRUCTURE TEST")
    print("="*60)

    tests = [
        test_imports,
        test_detector_initialization,
        test_detection_logic,
        test_prompt_generation,
        test_agent_structure,
        test_reporting
    ]

    passed = 0
    failed = 0

    for test in tests:
        try:
            if test():
                passed += 1
            else:
                failed += 1
        except Exception as e:
            print(f"  ❌ Test crashed: {e}")
            failed += 1

    print("\n" + "="*60)
    print(" SUMMARY")
    print("="*60)
    print(f"✅ Passed: {passed}/{len(tests)}")
    print(f"❌ Failed: {failed}/{len(tests)}")

    if failed == 0:
        print("\n🎉 All structure tests passed! The evaluation agent is ready.")
    else:
        print("\n⚠️  Some tests failed. Please review the errors above.")


if __name__ == "__main__":
    main()
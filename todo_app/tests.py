#!/usr/bin/env python3
"""
Run all component tests
"""

import subprocess
import sys


def run_test(test_file):
    """Run a single test file"""
    print(f"\n{'='*50}")
    print(f"Running {test_file}")
    print(f"{'='*50}")
    
    try:
        result = subprocess.run([sys.executable, test_file], 
                              capture_output=False, 
                              text=True)
        return result.returncode == 0
    except Exception as e:
        print(f"❌ Error running {test_file}: {e}")
        return False


def main():
    """Run all tests"""
    print("🧪 RUNNING ALL COMPONENT TESTS")
    print("="*60)
    
    test_files = [
        "test_models.py",
        "test_file_io.py", 
        "test_todo.py",
        "test_main.py"
    ]
    
    results = []
    
    for test_file in test_files:
        success = run_test(test_file)
        results.append((test_file, success))
    
    # Summary
    print(f"\n{'='*60}")
    print("📊 TEST SUMMARY")
    print(f"{'='*60}")
    
    passed = 0
    for test_file, success in results:
        status = "✅ PASSED" if success else "❌ FAILED"
        print(f"{test_file:20} {status}")
        if success:
            passed += 1
    
    print(f"\nTotal: {passed}/{len(test_files)} tests passed")
    
    if passed == len(test_files):
        print("🎉 All tests passed! Your components are working correctly!")
    else:
        print("⚠️  Some tests failed. Check the output above for details.")


if __name__ == "__main__":
    main()
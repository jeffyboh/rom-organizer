#!/usr/bin/env python3
"""
Test runner script for the ROM Library project.
"""

import subprocess
import sys
from pathlib import Path

def run_tests():
    """Run the test suite."""
    print("🧪 Running ROM Library Test Suite")
    print("=" * 50)

    # Check if we're in the right directory
    if not Path("pyproject.toml").exists():
        print("❌ Error: Please run this script from the project root directory")
        sys.exit(1)

    # Run pytest
    try:
        result = subprocess.run([
            sys.executable, "-m", "pytest",
            "tests/",
            "-v",
            "--tb=short",
            "--cov=app",
            "--cov-report=term-missing"
        ], capture_output=False, text=True)

        if result.returncode == 0:
            print("\n✅ All tests passed!")
        else:
            print(f"\n❌ Tests failed with exit code {result.returncode}")
            sys.exit(result.returncode)

    except FileNotFoundError:
        print("❌ Error: pytest not found. Please install testing dependencies:")
        print("   pip install -r requirements.txt")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n⚠️  Tests interrupted by user")
        sys.exit(1)

if __name__ == "__main__":
    run_tests()
import pytest
import sys
import os


def run_tests():
    """
    Run all pytest tests in the tests/ directory with coverage reporting for the rexa package.
    """
    # Ensure the project root is in sys.path to import rexa correctly
    project_root = os.path.abspath(os.path.dirname(__file__))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)

    # Define pytest arguments
    # -v: verbose output
    # --cov=rexa: generate coverage report for rexa package
    # --cov-report=term-missing: show missing lines in terminal
    # tests/: directory containing test files
    pytest_args = [
        "-v",
        "--cov=rexa",
        "--cov-report=term-missing",
        ""
    ]

    print("Running Rexa test suite...")
    exit_code = pytest.main(pytest_args)

    if exit_code == 0:
        print("All tests passed successfully!")
    else:
        print(f"Test suite completed with exit code {exit_code}. Some tests may have failed.")

    return exit_code


if __name__ == "__main__":
    sys.exit(run_tests())
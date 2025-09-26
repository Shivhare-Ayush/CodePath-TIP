#!/usr/bin/env python3
"""
Problem Runner Utility

A utility to run individual problems from CodePath TIP practice sessions.
This utility can work with any session file that follows the standard format.

Usage:
    python problem_runner.py Unit1/Session2.py                    # List all problems in Session2
    python problem_runner.py Unit1/Session2.py 1                  # Run problem 1
    python problem_runner.py Unit1/Session2.py transpose          # Run problem by name
    python problem_runner.py Unit1/Session2.py all               # Run all problems
"""
import sys
import os
import importlib.util
from pathlib import Path

def load_session_module(session_path):
    """Load a session file as a Python module"""
    if not os.path.exists(session_path):
        print(f"Error: File '{session_path}' not found!")
        return None
    
    # Get the module name from the file path
    module_name = Path(session_path).stem
    
    # Load the module
    spec = importlib.util.spec_from_file_location(module_name, session_path)
    if spec is None or spec.loader is None:
        print(f"Error: Could not load module from '{session_path}'")
        return None
    
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def run_session_problem(session_path, problem_identifier=None):
    """Run a problem from a session file"""
    module = load_session_module(session_path)
    if module is None:
        return False
    
    # Check if the module has the required functions
    if not hasattr(module, 'PROBLEMS'):
        print(f"Error: '{session_path}' doesn't follow the standard problem format!")
        print("Make sure the file has a PROBLEMS dictionary and problem functions.")
        return False
    
    if problem_identifier is None:
        # List problems
        if hasattr(module, 'list_problems'):
            module.list_problems()
        else:
            print("Available problems:")
            for num, (name, func) in module.PROBLEMS.items():
                print(f"  {num}. {func.__doc__} (name: {name})")
    elif problem_identifier.lower() == "all":
        # Run all problems
        if hasattr(module, 'run_all_problems'):
            module.run_all_problems()
        else:
            print("Running all problems:")
            print("=" * 50)
            for num, (_, func) in module.PROBLEMS.items():
                func()
    else:
        # Run specific problem
        if hasattr(module, 'run_problem'):
            success = module.run_problem(problem_identifier)
            if not success and hasattr(module, 'list_problems'):
                print()
                module.list_problems()
        else:
            # Fallback implementation
            try:
                problem_num = int(problem_identifier)
                if problem_num in module.PROBLEMS:
                    _, func = module.PROBLEMS[problem_num]
                    func()
                    return True
            except ValueError:
                pass
            
            # Try to find by name
            for num, (name, func) in module.PROBLEMS.items():
                if name.lower() == problem_identifier.lower():
                    func()
                    return True
            
            print(f"Problem '{problem_identifier}' not found!")
            return False
    
    return True

def main():
    """Main function to handle command line arguments"""
    if len(sys.argv) < 2:
        print("Usage: python problem_runner.py <session_file> [problem_number|problem_name|all]")
        print()
        print("Examples:")
        print("  python problem_runner.py Unit1/Session2.py")
        print("  python problem_runner.py Unit1/Session2.py 1")
        print("  python problem_runner.py Unit1/Session2.py transpose")
        print("  python problem_runner.py Unit1/Session2.py all")
        return
    
    session_path = sys.argv[1]
    problem_identifier = sys.argv[2] if len(sys.argv) > 2 else None
    
    run_session_problem(session_path, problem_identifier)

if __name__ == "__main__":
    main()
# Example Python practice file for Unit 1
# This demonstrates the recommended structure for organizing practice problems

import sys

def problem_1_hello_world():
    """Problem 1: Hello World Function"""
    print("Problem 1: Hello World Function")
    
    def hello_world():
        """
        A simple function to demonstrate Python practice in Unit 1
        """
        return "Hello, CodePath TIP 102!"
    
    # Test the function
    result = hello_world()
    print(f"Result: {result}")
    print()

def problem_2_example_calculation():
    """Problem 2: Example Calculation"""
    print("Problem 2: Example Calculation")
    
    def add_numbers(a, b):
        """
        Add two numbers together
        """
        return a + b
    
    # Test the function
    result = add_numbers(5, 3)
    print(f"5 + 3 = {result}")
    print()

# Problem registry for easy access
PROBLEMS = {
    1: ("hello_world", problem_1_hello_world),
    2: ("add_numbers", problem_2_example_calculation),
}

def list_problems():
    """List all available problems"""
    print("Available problems:")
    for num, (name, func) in PROBLEMS.items():
        print(f"  {num}. {func.__doc__} (name: {name})")
    print()

def run_problem(identifier):
    """Run a specific problem by number or name"""
    # Try to convert to int if it's a number
    try:
        problem_num = int(identifier)
        if problem_num in PROBLEMS:
            _, func = PROBLEMS[problem_num]
            func()
            return True
    except ValueError:
        pass
    
    # Try to find by name
    for num, (name, func) in PROBLEMS.items():
        if name.lower() == identifier.lower():
            func()
            return True
    
    print(f"Problem '{identifier}' not found!")
    return False

def run_all_problems():
    """Run all problems"""
    print("Running all problems:")
    print("=" * 50)
    for num, (_, func) in PROBLEMS.items():
        func()

if __name__ == "__main__":
    if len(sys.argv) == 1:
        # No arguments - list problems
        list_problems()
    elif len(sys.argv) == 2:
        arg = sys.argv[1].lower()
        if arg == "all":
            run_all_problems()
        else:
            success = run_problem(sys.argv[1])
            if not success:
                print()
                list_problems()
    else:
        print("Usage: python example_practice.py [problem_number|problem_name|all]")
        list_problems()
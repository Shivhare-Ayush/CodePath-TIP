# CodePath-TIP
A repo for all my problems I complete in codepath's TIP 102 Course 
https://courses.codepath.org/courses/tip102

## Folder Structure

This repository is organized by units, with each unit containing Python practice files:

- `Unit1/` - Unit 1 Python practice files
- `Unit2/` - Unit 2 Python practice files
- `Unit3/` - Unit 3 Python practice files
- `Unit4/` - Unit 4 Python practice files
- `Unit5/` - Unit 5 Python practice files
- `Unit6/` - Unit 6 Python practice files
- `Unit7/` - Unit 7 Python practice files
- `Unit8/` - Unit 8 Python practice files
- `Unit9/` - Unit 9 Python practice files
- `Unit10/` - Unit 10 Python practice files
- `Unit11/` - Unit 11 Python practice files
- `Unit12/` - Unit 12 Python practice files

Each unit folder contains its own README.md with specific instructions for that unit.

## Running Individual Problems

Each practice session file is structured so you can run individual problems instead of executing all problems at once. This helps you focus on specific problems during practice.

### Method 1: Using the Session File Directly

Navigate to any session file and run it with optional arguments:

```bash
# List all problems in the session
python Unit1/Session2.py

# Run a specific problem by number
python Unit1/Session2.py 1

# Run a specific problem by name
python Unit1/Session2.py transpose

# Run all problems
python Unit1/Session2.py all
```

### Method 2: Using the Problem Runner Utility

Use the `problem_runner.py` utility for a consistent interface across all session files:

```bash
# List all problems in Session2
python problem_runner.py Unit1/Session2.py

# Run problem 1 from Session2
python problem_runner.py Unit1/Session2.py 1

# Run problem by name from Session2
python problem_runner.py Unit1/Session2.py transpose

# Run all problems from Session2
python problem_runner.py Unit1/Session2.py all
```

### File Structure for Practice Sessions

Each practice session file follows this structure:

1. **Problem Functions**: Each problem is wrapped in its own function (e.g., `problem_1_transpose()`)
2. **Problem Registry**: A `PROBLEMS` dictionary maps numbers and names to functions
3. **Command Line Interface**: Uses `sys.argv` to handle different run modes
4. **Main Guard**: Uses `if __name__ == "__main__":` to prevent auto-execution when imported

This structure allows you to:
- Focus on one problem at a time
- Quickly test specific algorithms
- Avoid scrolling through output from all problems
- Easily compare different approaches to the same problem

### Example Usage

```bash
# Work on just the transpose matrix problem
python Unit1/Session2.py 1

# Practice the reverse list algorithm
python Unit1/Session2.py reverse

# Run all problems to review your solutions
python Unit1/Session2.py all
```

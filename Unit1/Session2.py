# Strings and Arrays
'''
Purpose is to practice UPI method to solve problems. 
if you need help use this cheatsheet: https://courses.codepath.org/courses/tip102/unit/1#!cheatsheet

Usage:
    python Session2.py                    # List all problems
    python Session2.py 1                  # Run problem 1
    python Session2.py transpose          # Run problem 1 by name
    python Session2.py all                # Run all problems
'''
import sys

def problem_1_transpose():
    """Problem 1: Transpose Matrix"""
    print("Problem 1: Transpose Matrix")
    
    def transpose(matrix):
        '''Understand: Given a 2D array, we transpose the matrix.
        Input: 2D array (list of lists)
        Transpose: Switch rows with columns
        Plan: Create a new matrix with switched dimensions, then fill it in.'''
        new_matrix = []
        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0
        for col in range(cols):
            new_row = []
            for row in range(rows):
                new_row.append(matrix[row][col])
            new_matrix.append(new_row)
        return new_matrix
    
    # Test the function
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print("Original Matrix:", matrix)
    print("Transposed Matrix:", transpose(matrix)) # [[1,4,7],[2,5,8],[3,6,9]]
    print()

def problem_2_reverse():
    """Problem 2: Reverse List using 2 pointer technique"""
    print("Problem 2: Reverse List")
    
    def reverse_list(lst):
        '''Understand: Given a list, we reverse it in place.
        Input: List (1D array)
        Reverse: Switch elements from start to end
        Plan: Use two pointers to swap elements.'''
        left = 0
        right = len(lst) - 1
        while left < right:
            lst[left], lst[right] = lst[right], lst[left]
            left += 1
            right -= 1
        return lst
    
    # Test the function
    list_to_reverse = [1,2,3,4,5]
    print("Original List:", list_to_reverse)
    print("Reversed List:", reverse_list(list_to_reverse.copy())) # [5,4,3,2,1]
    print()

def problem_3_remove_duplicates():
    """Problem 3: Remove Duplicates from Sorted Array"""
    print("Problem 3: Remove Duplicates from Sorted Array")
    
    def remove_duplicates(sorted_array):
        '''Understand: Given a sorted array, we remove duplicates in place.
        Input: Sorted list (1D array)
        Remove Duplicates: Keep only unique elements
        Plan: Use two pointers to overwrite duplicates.'''
        if not sorted_array:
            return 0
        write_index = 1
        for i in range(1, len(sorted_array)):
            if sorted_array[i] != sorted_array[i - 1]:
                sorted_array[write_index] = sorted_array[i]
                write_index += 1
        return sorted_array[:write_index]
    
    # Test the function
    sorted_array = [1,2,3,4,4,5]
    print("Original Sorted Array:", sorted_array)
    print("Array after removing duplicates:", remove_duplicates(sorted_array.copy())) # [1,2,3,4,5]
    print()

def problem_4_sort_parity():
    """Problem 4: Sort Array by Parity"""
    print("Problem 4: Sort Array by Parity")
    
    def sort_array_by_parity(arr):
        ''' Understand: Given an array, sort it by PARITY (even numbers first).
        Input: List (1D array)
        Sort by Parity: Even numbers first, then odd numbers
        Plan: Use two pointers to partition the array.'''
        insert_index = 0
        for i in range(len(arr)):
            if arr[i] % 2 == 0:
                arr[i], arr[insert_index] = arr[insert_index], arr[i] # swap 
                insert_index += 1
        return arr
    
    # Test the function
    array_to_sort = [3,1,2,4]
    print("Original Array:", array_to_sort)
    print("Array sorted by parity:", sort_array_by_parity(array_to_sort.copy())) # [2,4,3,1]
    print()

def problem_5_container_honey():
    """Problem 5: Container with Most Honey"""
    print("Problem 5: Container with Most Honey")
    def container_with_most_honey(heights):
        '''
        Understand: Given an array of heights, find two lines that together with the x-axis form a container that holds the most water.
        Input: List of heights (1D array)
        Plan: Use two pointers to find the maximum area.
        '''
        left = 0
        right = len(heights) - 1
        max_area = 0
        while left < right:
            if heights[left] < heights[right]:
                area = heights[left] * (right - left)
                left += 1
            else:
                area = heights[right] * (right - left)
                right -= 1
            max_area = max(max_area, area)
        return max_area
    # Test the function
    print("Heights:", [1,8,6,2,5,4,8,3,7])
    print("Max area:", container_with_most_honey([1,8,6,2,5,4,8,3,7]))

def problem_6_merge_intervals():
    """Problem 6: Merge Intervals"""
    print("Problem 6: Merge Intervals")
    def merge_intervals(intervals):
        ''' understand: given a 2D array intervals, we need to merge overlaping ranges
            input: 2D array intervals
            merge: if intervals[i][1] > intervals[n][0] and intervals[i][0] <  intervals[n][0]
            return: intervals[i][0] + max(intervals[i][1], intervals[n][1])
            ** assume intervals are sorted by start amount
        '''
        n = len(intervals)
        for i in range(n-1):
            j = i+1
            in_1 = intervals[i]
            while j < n:
                in_2 = intervals[j] 
                if  in_1[1] >= in_2[0]:
                    new_end = max(in_2[1], in_1[1])
                    intervals[i][1] = new_end
                    in_1 = intervals[i]
                    del(intervals[j])     
                    n = len(intervals)            
                else:
                    break
        return intervals
    print()
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    #intervals = [[1, 4], [4, 5]]
    print('intervals', intervals)
    print("merged:", merge_intervals(intervals))
# Problem registry for easy access
PROBLEMS = {
    1: ("transpose", problem_1_transpose),
    2: ("reverse", problem_2_reverse),
    3: ("remove_duplicates", problem_3_remove_duplicates),
    4: ("sort_parity", problem_4_sort_parity),
    5: ("container_honey", problem_5_container_honey),
    6: ("merge_intervals", problem_6_merge_intervals),
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
        print("Usage: python Session2.py [problem_number|problem_name|all]")
        list_problems()

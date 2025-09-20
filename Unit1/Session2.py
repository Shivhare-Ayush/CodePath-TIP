# Strings and Arrays
'''
Purpose is to practice UPI method to solve problems. 
if you need help use this cheatsheet: https://courses.codepath.org/courses/tip102/unit/1#!cheatsheet
'''

# Problem 1: Transpose Matrix
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
# --
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print("Original Matrix:", matrix)
print("Transposed Matrix:", transpose(matrix)) # [[1,4,7],[2,5,8],[3,6,9]]

# Problem 2: 2 pointer reverse list
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
# --
list_to_reverse = [1,2,3,4,5]
print("Original List:", list_to_reverse)
print("Reversed List:", reverse_list(list_to_reverse)) # [5,4,3,2,1]

# Problem 3: Remove Duplicates from Sorted Array
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
# --
sorted_array = [1,2,3,4,4,5]
print("Original Sorted Array:", sorted_array)
print("Array after removing duplicates:", remove_duplicates(sorted_array)) # [1,2,3,4,5]

# Problem 4: Sort Array by Parity
# Problem 5: Container with Most Honey
# Problem 6: Merge Intervals

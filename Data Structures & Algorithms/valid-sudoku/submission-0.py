'''
u- We must check 3 conditions. No repeating numbers in any row, column, or 3 x 3 grid.
m - No duplicates = set. 
p - 
i - 
r - 
e - 
'''
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        n = 9
        #for row in range(n):
        #    print(board[row])

        squares = [set(), set(), set(), set(), set(), set(), set(), set(), set()]
        for row in range(n):
            for col in range(n):
                num = board[row][col] 
                if num != '.':
                    square = int(row / 3) * 3 + int(col / 3)
                    if num in squares[square]:
                        print(f'found {num} in {squares[square]}')
                        return False
                    squares[square].add(num)
        # rows checked
        
        for row in range(n):
            row_check = set()
            for col in range(n):
                num = board[row][col]
                if num != '.':
                    if num in row_check:
                        print(f'found {num} in {row_check}')
                        return False
                    row_check.add(num)

        # col check 
        for col in range(n):
            col_check = set()
            for row in range(n):
                num = board[row][col]
                if num != '.':
                    if num in col_check:
                        print(f'found {num} in {col_check}')
                        return False
                    col_check.add(num)
            
    
        
        return True
        
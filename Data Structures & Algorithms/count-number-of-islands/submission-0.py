'''
Adjacency list: For every node your reachable nodes are just the immediate 4 

traverse legal moves of a point. Once we run out of moves we conclude an island and move on. 
After an island is discovered use two conditions (visited, and water) to determine next place to traverse. 
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        max_rows = len(grid)
        max_cols = len(grid[0])
        islands = 0
        def explore(y, X):
            stack = []
            stack.append((y, X))
            while stack:
                y, X = stack.pop()
                visited.add((y, X))
                print(y, X)

                #visited.add(node) # add to visited
                if y-1 in range(max_rows) and grid[y-1][X] == "1" and (y-1, X) not in visited:
                    stack.append((y-1, X)) #left
                if y+1 in range(max_rows) and grid[y+1][X] == "1" and (y+1, X) not in visited:
                    stack.append((y+1, X)) #right
                if X+1 in range(max_cols) and grid[y][X+1] == "1" and (y, X+1) not in visited:
                    stack.append((y, X+1)) #up
                if X-1 in range(max_cols) and grid[y][X-1] == "1" and (y, X-1) not in visited:
                    stack.append((y, X-1)) #down
        
        visited = set()
        for r in range(max_rows):
            for c in range(max_cols):
                location = (r, c)
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    explore(r, c)
        print(visited)
        return islands



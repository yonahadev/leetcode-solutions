class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        gridWidth = len(grid)
        for x in range(gridWidth): #row
            rowHeight = len(grid[x])
            for y in range(rowHeight): #column
                isLand = grid[x][y] == 1
                if isLand: 
                    if x == 0:
                        perimeter += 1
                    if x == gridWidth-1:
                        perimeter += 1
                    if x > 0: 
                        if grid[x-1][y] == 0:
                            perimeter += 1
                    if x < gridWidth-1:
                        if grid[x+1][y] == 0: 
                            perimeter += 1
                    
                    if y == 0: 
                        perimeter += 1
                    if y == rowHeight-1:
                        perimeter += 1
                    if y > 0: 
                        if grid[x][y-1] == 0: 
                            perimeter += 1
                    if y < rowHeight-1:
                        if grid[x][y+1] == 0: 
                            perimeter += 1
        return perimeter

# Run the same script multiple times to get multiple grid solutions in terminal
# Feel free to input your own solvable* sudoku puzzle into the grid, keeping grid structure the same.

import numpy as np

grid = [[2,9,5,7,0,0,8,0,1],
        [4,0,0,8,6,0,9,0,0],
        [0,7,6,0,0,0,5,4,3],
        [3,0,0,4,5,9,2,1,0],
        [0,1,2,0,8,0,4,9,5],
        [5,0,9,2,0,0,0,0,8],
        [0,0,3,0,3,0,1,8,9],
        [9,2,0,0,7,0,0,0,4],
        [1,0,4,9,3,0,6,0,0]]

def possible(row, column, number):
    global grid
    #Is the number appearing in the given row?
    for i in range(0,9):
        if grid[row][i] == number:
            return False

    #Is the number appearing in the given column?
    for i in range(0,9):
        if grid[i][column] == number:
            return False
  
    #Is the number appearing in the given square? (divide the current number by 3, then round it down to the closest number)
    x0 = (column // 3) * 3
    y0 = (row // 3) * 3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j] == number:
                return False

    return True

def solve():
    global grid
    for row in range(0,9):
        for column in range(0,9):
            if grid[row][column] == 0:
                for number in range(1,10):
                    if possible(row, column, number):
                        grid[row][column] = number
                        solve()
                        grid[row][column] = 0

                return

    print(np.matrix(grid))
    input('More possible solutions')

solve()

   
   
    # We divide the grid into sections going down, there is section 0, then section 1, then section 2
    # We want to start the 0 section from row 0 
    # the 1st section from row 3 
    # and the 2nd section from row 6

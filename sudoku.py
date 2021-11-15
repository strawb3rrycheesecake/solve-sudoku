import numpy as np
grid = np.array([
        [-1, -1, -1,   -1, 2, -1,   6, -1, -1],
        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [3, 8, -1,   7, -1, -1,   -1, -1, 2],

        [-1, -1, 6,   4, -1, -1,   -1, -1, -1],
        [8, 4, -1,   -1, -1, 3,   9, -1, -1],
        [-1, -1, 5,   -1, -1, -1,   -1, -1, 8],

        [-1, -1, 4,   -1, -1, -1,   -1, -1, -1],
        [2, 7, -1,   3, -1, -1,   -1, -1, 6],
        [-1, -1, -1,   -1, -1, 9,   -1, 1, -1]
    ])   
                


value = np.linspace(1,9,9)
print(value)

def nxt_empt(puzzle):
    #what this will do is find the next tile that == -1
    for r in range(9):
        for c in range(9):
            if puzzle[r,c] == -1:
                return r,c #returns row and column of a valid location
            
    return None, None

def is_valid(puzzle,guess,row,col):
    #lets start with row. 
    #here if the guess is already in the row, then the guess is not valid
    if guess in puzzle[row]:
        return False

    #next is the same thing but moving on to column
    if guess in puzzle[:,col]:
        return False 

    #next is the tricky 3 by 3 square bit
    x = (row // 3) *3
    y = (col // 3) *3
    if guess in puzzle[x:(x+3),y:(y+3)]:
        return False
   
            

    return True




def solve(puzzle):
    
    row, col = nxt_empt(puzzle)
    if row == None:
        return True #if there are no more valid spaces .ie spaces that are == -1, then the puzzle is complete

    for guess in value:
        if is_valid(puzzle,guess,row,col):
            #assuing that this returns true
            puzzle[row][col] = guess

            #now we want to repeat this steps again, hence we execute this function again
            if solve(puzzle):
                return True
        
        
        
        puzzle[row][col] = -1
        
    return False



    
print(solve(grid))
print(grid)
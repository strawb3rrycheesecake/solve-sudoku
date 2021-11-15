# solve-sudoku
Create a script to solve sudoku puzzles

I have to first create a 9 by 9 sudoku grid. A sudoku puzzle will have empty spaces and filled squares which serves as clues. For the empty spaces in the grid, I assign a value of -1.

My first function is nxt_empt(), which helps to find the next empty space in the grid, or in this case, the next position with a value of -1.

My second function is is_valid(). Once I have found an empty square, I have to see what values are valid for the square based on the 3 criterias in sudoku.
1. There must not be a repeat of this value in the row.
2. There must not be a repeat of this value in the column.
3. There must not be a repeat of this value in the 3 by 3 grid that this square is in.
The funciton is_valid() helps to cycle through the values 1 through 9 to find the value that fits the above criteria

Lastly, I had to put the 2 functions above together, so that it can continuously find empty spots and determine valid values for said spots. The function also has to reset the value of a certain spot back to -1 if it determines that its guess is incorrect.

Hence, the last function solve() puts the 2 earlier functions together, to solve the puzzle.

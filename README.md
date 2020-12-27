# Suduko
Sudoku is solved by backtracking algorithm.
Rules of a Sudoku Puzzle
1. It contains a 9 x 9 puzzle grid sub-divided into 3 x 3 blocks of 9 numbers.
2. Each number of any cell in the 9 x 9 puzzle can only be a number between 1 to 9, both inclusive.
3. Each 3 x 3 block should have all the numbers between 1 to 9 in any cell. As a 3 x 3 block has 9 cells, it’s obvious that no number can repeat.
4. Similarly each row of the 9 x 9 puzzle must have all the numbers between 1 to 9. Again, as each row has 9 cells, no number can repeat.
5. Each column needs to have the numbers between 1 to 9 as well and as above, no number can repeat.

Once we completely filled in a Sudoku Puzzle satisfying all the above criteria, we can safely assume that the puzzle has been solved.


Its writtten in Python

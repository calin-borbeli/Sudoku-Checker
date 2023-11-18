# Sudoku-Checker-Python-Essentials-2-Lab

Sudoku is a number-placing puzzle played on a 9x9 board. The player has to fill the board in a very specific way:

- each row of the board must contain all unique digits from 1 to 9 (the order doesn't matter)

- each column of the board must contain all unique digits from 1 to 9 (again, the order doesn't matter)

- each of the nine 3x3 "tiles" ("sub-squares") of the table must contain all unique digits from 1 to 9.

The program reads 9 rows of the Sudoku, each containing 9 digits checking if the data entered are valid then outputs OK if the Sudoku is valid for each rows, columns and tiles, or otherwise indicates the invalid rows, columns or tiles.

Example 1:

Valid Entries:

```Enter row [1]: 295743861
Enter row [2]: 431865927
Enter row [3]: 876192543
Enter row [4]: 387459216
Enter row [5]: 612387495
Enter row [6]: 549216738
Enter row [7]: 763524189
Enter row [8]: 928671354
Enter row [9]: 154938672```

Result:

```All rows are OK
All columns are OK
All tiles are OK```

Example 2:

Invalid entries:

```Enter row [1]: 295743861

Enter row [2]: 431865927

Enter row [3]: 876192543

Enter row [4]: 387459216

Enter row [5]: 612387495

Enter row [6]: 549216738

Enter row [7]: 76352418a

Enter row [8]: 928671324

Enter row [9]: 154938672```

Result:

```Invalid row [7]: '76352418a'

Invalid row [8]: '928671324'

Invalid column [8]: '624193827'

Invalid column [9]: '173658a42'

Invalid tile [7][7] to [9][9]: '18a324672'

```

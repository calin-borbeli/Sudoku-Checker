# Define function to check the groups of all unique digits from 1 to 9
def digit_check(group):
    if group.isdigit() and len(group) == 9:
        for d in range(1, 10):
            if str(d) not in group:
                return False
        return True


# Prepare empty rows list
rows = []
for i in range(9):
    # input the rows and append them to the list
    row = input("Enter row [" + str(i + 1) + "]: ")
    rows.append(row)


# Check that the rows contain only valid digits rows
rows_ok = True
for row in rows:
    if not digit_check(row):
        print("Invalid row [" + str(rows.index(row) + 1) + "]: '" + row + "'")
        rows_ok = False
if rows_ok:
    print("All rows are OK")

# Check that the columns contain only valid digits columns
cols_ok = True
for col in range(9):
    column = "".join(rows[row_col][col] for row_col in range(9))
    if not digit_check(column):
        print("Invalid column [" + str(col + 1) + "]: '" + column + "'")
        cols_ok = False
if rows_ok:
    print("All columns are OK")

# Check that the 3x3 tiles contain only valid digits tiles
tiles_ok = True
for tile_rows in range(0, 9, 3):
    for tile_cols in range(0, 9, 3):
        tile = []
        for rt in range(3):
            for ct in range(3):
                tile.append(rows[rt + tile_rows][ct + tile_cols])
        tile = "".join(tile)
        if not digit_check(tile):
            print(
                "Invalid tile ["
                + str(tile_cols + 1)
                + "]["
                + str(tile_rows + 1)
                + "] to ["
                + str(ct + tile_cols + 1)
                + "]["
                + str(rt + tile_rows + 1)
                + "]: '"
                + tile
                + "'"
            )
            tiles_ok = False
if tiles_ok:
    print("All tiles are OK")

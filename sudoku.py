# Define function to check the groups of all unique digits from 1 to 9
def digit_check(group):
    if len(group) == 9:
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
print(rows)


# Check that the rows contain only valid digits rows
for row in rows:
    if not digit_check(row):
        print("Invalid row [" + str(rows.index(row)) + "]: '" + row + "'")

# Check that the columns contain only valid digits columns
for c in range(9):
    column = "".join(rows[rc][c] for rc in range(9))
    if not digit_check(column):
        print("Invalid column [" + str(c + 1) + "]: '" + column + "'")

# Check that the 3x3 tiles contain only valid digits tiles

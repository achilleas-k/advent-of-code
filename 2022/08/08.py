import sys


fname = sys.argv[1]

height_map = []

with open(fname, encoding="utf-8") as infile:
    for line in infile:
        row = [int(height) for height in line.strip()]
        height_map.append(row)

# iterate using indices to save coords while moving
ncols = len(height_map[0])
nrows = len(height_map)

visible = set()

# left to right
for rowidx in range(nrows):
    highest = -1
    for colidx in range(ncols):
        if height_map[rowidx][colidx] > highest:
            visible.add((rowidx, colidx))
            highest = height_map[rowidx][colidx]

# right to left
for rowidx in range(nrows):
    highest = -1
    for colidx in range(ncols-1, -1, -1):
        if height_map[rowidx][colidx] > highest:
            visible.add((rowidx, colidx))
            highest = height_map[rowidx][colidx]

# top to bottom
for colidx in range(ncols):
    highest = -1
    for rowidx in range(nrows):
        if height_map[rowidx][colidx] > highest:
            visible.add((rowidx, colidx))
            highest = height_map[rowidx][colidx]

# bottom to top
for colidx in range(ncols):
    highest = -1
    for rowidx in range(nrows-1, -1, -1):
        if height_map[rowidx][colidx] > highest:
            visible.add((rowidx, colidx))
            highest = height_map[rowidx][colidx]

print("Part 1")
print(f"{len(visible)} trees are visible from outside")

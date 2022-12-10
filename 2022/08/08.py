import sys


fname = sys.argv[1]

height_map = []
scenic_map = []


def print_map(m):
    """
    Print a map for troubleshooting.
    """
    print("\n".join("".join(str(v) for v in r) for r in m))


with open(fname, encoding="utf-8") as infile:
    for line in infile:
        row = [int(height) for height in line.strip()]
        height_map.append(row)
        scenic_map.append([0]*len(row))

# iterate using indices to save coords while moving
ncols = len(height_map[0])
nrows = len(height_map)

visible = set()

# counters
highest = 0
height_scenicness = []  # tracks the distance a tree of a given height can see


def reset():
    """
    Reset the counters
    """
    global highest, height_scenicness
    highest = -1
    height_scenicness = [0] * 10


def update(rowidx, colidx, first=False):
    """
    Update the counters: highest so far and scenicness
    """
    global highest, height_scenicness, visible
    tree_height = height_map[rowidx][colidx]
    if tree_height > highest:
        visible.add((rowidx, colidx))
        highest = tree_height

    if first:
        scenic_map[rowidx][colidx] = height_scenicness[tree_height]
    else:
        scenic_map[rowidx][colidx] *= height_scenicness[tree_height]

    # reset the scenicness of all trees shorter or equal to the current one
    height_scenicness[:tree_height+1] = [0] * (tree_height+1)

    # increment the scenicness for everyone
    for idx in range(10):
        height_scenicness[idx] += 1


# left to right
for rowidx in range(nrows):
    reset()
    for colidx in range(ncols):
        update(rowidx, colidx, first=True)


# right to left
for rowidx in range(nrows):
    reset()
    for colidx in range(ncols-1, -1, -1):
        update(rowidx, colidx)

# top to bottom
for colidx in range(ncols):
    reset()
    for rowidx in range(nrows):
        update(rowidx, colidx)

# bottom to top
# last pass: track highest scenic score
max_scenic = 0
for colidx in range(ncols):
    reset()
    for rowidx in range(nrows-1, -1, -1):
        update(rowidx, colidx)

        if scenic_map[rowidx][colidx] > max_scenic:
            max_scenic = scenic_map[rowidx][colidx]


print("Part 1")
print(f"{len(visible)} trees are visible from outside")

print("Part 2")
print(f"{max_scenic} is the highest scenic score possible")

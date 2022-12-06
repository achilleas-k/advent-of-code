import sys


fname = sys.argv[1]


def first_marker_index(line: str, mlen: int) -> int:
    for idx in range(len(line)):
        # mlen char sliding window
        win = line[idx:idx+mlen]
        if len(set(win)) == len(win):
            return idx+mlen

    raise RuntimeError("no marker found")


with open(fname, encoding="utf-8") as infile:
    # the real input is one line long but let's iterate so we can run all the examples from a single file
    for line in infile:
        print(f"Part 1: {first_marker_index(line, 4)}")
        print(f"Part 2: {first_marker_index(line, 14)}")
        print("--")

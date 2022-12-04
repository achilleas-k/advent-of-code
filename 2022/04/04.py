import sys
from typing import Tuple


fname = sys.argv[1]

Range = Tuple[int, int]


def parse_range(rng: str) -> Range:
    elems = rng.split("-")
    if len(elems) != 2:
        raise ValueError(f"[parse_range] bad range string: {rng}")

    start, end = elems
    return int(start), int(end)


def parse_line(line: str) -> Tuple[Range, Range]:
    ranges = line.split(",")
    if len(ranges) != 2:
        raise ValueError(f"[split_line] bad input line: {line}")

    return parse_range(ranges[0]), parse_range(ranges[1])


def superset(a: Range, b: Range) -> bool:
    if a[0] <= b[0] and a[1] >= b[1]:
        # a fully contains b
        return True

    if a[0] >= b[0] and a[1] <= b[1]:
        # b fully contains a
        return True

    return False


def overlap(a: Range, b: Range) -> bool:
    if superset(a, b):
        # get that out of the way
        return True

    if a[0] <= b[0] and a[1] >= b[0]:
        return True

    if a[0] >= b[0] and a[0] <= b[1]:
        return True

    return False


supersets = 0
overlaps = 0
with open(fname, encoding="utf-8") as infile:
    for line in infile:
        line = line.strip()
        range_a, range_b = parse_line(line)
        supersets += superset(range_a, range_b)
        overlaps += overlap(range_a, range_b)

print(f"Supersets: {supersets}")
print(f"Overlaps:  {overlaps}")

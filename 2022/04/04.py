import sys
from typing import Tuple


fname = sys.argv[1]


def parse_range(rng: str) -> Tuple[int, int]:
    elems = rng.split("-")
    if len(elems) != 2:
        raise ValueError(f"[parse_range] bad range string: {rng}")

    start, end = elems
    return int(start), int(end)


def split_line(line: str) -> Tuple[str, str]:
    ranges = line.split(",")
    if len(ranges) != 2:
        raise ValueError(f"[split_line] bad input line: {line}")

    return ranges[0], ranges[1]


def superset(a: Tuple[int, int], b: Tuple[int, int]) -> bool:
    if a[0] <= b[0] and a[1] >= b[1]:
        # a fully contains b
        return True

    if a[0] >= b[0] and a[1] <= b[1]:
        # b fully contains a
        return True

    return False


overlaps = 0
with open(fname, encoding="utf-8") as infile:
    for line in infile:
        line = line.strip()
        range_a, range_b = split_line(line)
        overlaps += superset(parse_range(range_a), parse_range(range_b))

print(overlaps)

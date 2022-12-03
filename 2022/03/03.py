import sys

fname = sys.argv[1]


def find_wrong_item(items: str) -> str:
    """
    Find the item that is in both compartments (both halves of the string).
    """
    if len(items) % 2 > 0:
        raise ValueError(f"[find_wrong_item] item string has odd length: {items}")

    half = len(items) // 2

    comp_a, comp_b = items[:half], items[half:]

    common_char = set(comp_a).intersection(set(comp_b))
    if len(common_char) > 1:  # sanity check
        raise RuntimeError("[find_wrong_item] found more than one common item: this shouldn't happen")

    return common_char.pop()


def item_priority(item: str) -> int:
    """
    Get item's priority value.
    """
    if len(item) != 1:
        raise ValueError(f"[item_priority] item {item} invalid: should be single character")

    if "A" <= item <= "Z":
        return ord(item) - 38

    if "a" <= item <= "z":
        return ord(item) - 96

    raise ValueError(f"[item_priority] item {item} invalid: must be [a-zA-Z]")


print(f"Using data from {fname}")

priority_sums = 0
with open(fname, encoding="utf-8") as infile:
    for idx, line in enumerate(infile):
        priority = item_priority(find_wrong_item(line.strip()))
        priority_sums += priority

print(f"Part 1: Sum of priorities of incorrectly packed items: {priority_sums}")

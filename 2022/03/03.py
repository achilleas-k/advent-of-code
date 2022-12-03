import sys

from typing import List


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


def find_group_badge(group_items: List[str]) -> str:
    """
    Find the item that represents the 3-elf group: The single common item between all three.
    """
    if (length := len(group_items)) != 3:
        raise ValueError(f"[find_group_badge] group_items has wrong length: {length}")

    common_char = set(group_items[0]).intersection(set(group_items[1])).intersection(set(group_items[2]))
    if len(common_char) > 1:  # sanity check
        raise RuntimeError("[find_group_badge] found more than one common item: this shouldn't happen")

    return common_char.pop()


print(f"Using data from {fname}")

wrong_item_sum = 0
group_sum = 0

group = []
with open(fname, encoding="utf-8") as infile:
    for line in infile:
        wrong_item_sum += item_priority(find_wrong_item(line.strip()))

        group.append(line.strip())
        if len(group) % 3 == 0:  # group every three lines
            group_sum += item_priority(find_group_badge(group))
            group = []

print(f"Part 1: Sum of priorities of incorrectly packed items: {wrong_item_sum}")
print(f"Part 2: Sum of priorities of group badges: {group_sum}")

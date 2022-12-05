import re
import sys

from typing import Dict, List, Optional


fname = sys.argv[1]
part = sys.argv[2]

Stacks = Dict[int, List[str]]
Move = Dict[str, int]


def parse_crate_row(line: str) -> Optional[List[str]]:
    """
    Parse the input to identify crate positions in a row.  Returns a list of crate names (single characters).  Empty
    strings represent empty stacks.

    If it's not a crate line, returns None.
    """
    if "[" not in line:
        # No crates
        return None

    crates = []
    for col in range(1, len(line), 4):
        crates.append(line[col])

    return crates


move_regex = re.compile(r"move (?P<move>[0-9]+) from (?P<from>[0-9]+) to (?P<to>[0-9]+)")


def parse_move_row(line: str) -> Optional[Move]:
    """
    Parse the input to identify move orders.  Returns a dictionary with three keys:
    - move: number of crates to move
    - from: stack to move crates from
    - to: stack to move crates to

    If it's not a move line, returns None.
    """
    matches = move_regex.match(line)
    if matches:
        return {
            "move": int(matches["move"]),
            "from": int(matches["from"]),
            "to": int(matches["to"]),
        }

    return None


def perform_move_9000(stacks: Stacks, move: Move) -> Stacks:
    """
    Performs the given move as the CrateMover 9000 on the given stack and returns the new stack state.
    """
    from_stack = move["from"]
    to_stack = move["to"]
    for move_num in range(move["move"]):
        crate = stacks[from_stack].pop(0)  # remove from top
        stacks[to_stack].insert(0, crate)  # add to top
    return stacks


def perform_move_9001(stacks: Stacks, move: Move) -> Stacks:
    """
    Performs the given move as the CrateMover 9001 on the given stack and returns the new stack state.
    """
    from_stack = move["from"]
    to_stack = move["to"]
    move_crates = move["move"]

    stack = stacks[from_stack]

    # split the stack into mover and remaining
    mover = stack[:move_crates]
    stack = stack[move_crates:]

    # put back the remaining stack
    stacks[from_stack] = stack

    # prepend the mover crates onto the destination stack
    mover.extend(stacks[to_stack])
    stacks[to_stack] = mover

    return stacks


def print_tops(stacks: Stacks):
    tops = []
    for stack_num in sorted(stacks.keys()):
        stack = stacks[stack_num]
        tops.append(stack[0])

    print("".join(tops))


stacks: Dict[int, List[str]] = {}
moves = []
with open(fname, encoding="utf-8") as infile:
    for line in infile:
        if crates := parse_crate_row(line):
            for idx, crate in enumerate(crates, 1):
                if crate == " ":
                    # skip empty crate slots
                    continue
                stack = stacks.get(idx, [])
                stack.append(crate)
                stacks[idx] = stack
        else:
            break

    for line in infile:
        if move := parse_move_row(line):
            moves.append(move)


print([stacks[k] for k in sorted(stacks.keys())])
print(moves)

if part == "a":
    for move in moves:
        stacks = perform_move_9000(stacks, move)
elif part == "b":
    for move in moves:
        stacks = perform_move_9001(stacks, move)
else:
    ValueError(f"unknown part: {part} ('a' or 'b')")

print([stacks[k] for k in sorted(stacks.keys())])

print_tops(stacks)

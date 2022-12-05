import re
import sys

from typing import Dict, List, Optional


fname = sys.argv[1]

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

    num_stacks = len(line)//4
    crates = []
    for col in range(num_stacks):
        crate = line[col*4+1:(col+1)*4-2]
        crates.append(crate)

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


def perform_move(stacks: Stacks, move: Move) -> Stacks:
    """
    Performs the given move on the given stack and returns the new stack state.
    """
    from_stack = move["from"]
    to_stack = move["to"]
    for move_num in range(move["move"]):
        crate = stacks[from_stack].pop(0)  # remove from top
        stacks[to_stack].insert(0, crate)  # add to top
    return stacks


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

for move in moves:
    stacks = perform_move(stacks, move)

print([stacks[k] for k in sorted(stacks.keys())])

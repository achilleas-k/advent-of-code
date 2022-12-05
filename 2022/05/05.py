import re
import sys

from typing import Dict, List, Optional


fname = sys.argv[1]


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


def parse_move_row(line: str) -> Optional[Dict[str, int]]:
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


def perform_move(stacks: List[List[str]], move: Dict[str, int]) -> List[List[str]]:
    """
    Performs the given move on the given stack and returns the new stack state.
    """
    return stacks


stacks = []
moves = []
with open(fname, encoding="utf-8") as infile:
    for line in infile:
        if crates := parse_crate_row(line):
            stacks.append(crates)
        else:
            break

    for line in infile:
        if move := parse_move_row(line):
            moves.append(move)


print(stacks)
print(moves)

for move in moves:
    stacks = perform_move(stacks, move)

print(stacks)

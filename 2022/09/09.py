import sys
from typing import Tuple, Set


fname = sys.argv[1]

Coords = Tuple[int, int]


def move_head(direction: str, position: Coords) -> Coords:
    if direction == "U":
        return position[0], position[1] + 1

    if direction == "D":
        return position[0], position[1] - 1

    if direction == "R":
        return position[0] + 1, position[1]

    if direction == "L":
        return position[0] - 1, position[1]

    raise ValueError(f"invalid direction: {direction}")


def distance(a: Coords, b: Coords) -> int:
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def calc_direction(source: Coords, dest: Coords) -> Coords:
    """
    Find the direction that make 'source' move closed to 'dest'.
    """
    xmove = 0
    ymove = 0

    if source[0] < dest[0]:
        # move right
        xmove = 1
    elif source[0] > dest[0]:
        # move left
        xmove = -1

    if source[1] < dest[1]:
        # move up
        ymove = 1
    elif source[1] > dest[1]:
        # move down
        ymove = -1

    return xmove, ymove


def move_tail(tail_pos: Coords, head_pos: Coords) -> Coords:
    if distance(tail_pos, head_pos) <= 2:
        # no move necessary
        return tail_pos

    move = calc_direction(tail_pos, head_pos)

    return tail_pos[0] + move[0], tail_pos[1] + move[1]


def parse_line(line: str) -> Tuple[str, int]:
    parts = line.split(" ")
    if len(parts) != 2:
        raise ValueError(f"line {line} looks invalid: more than two parts")
    return parts[0], int(parts[1])


head_pos = (0, 0)
tail_pos = (0, 0)
visited: Set[Coords] = set()
with open(fname, encoding="utf-8") as infile:
    for line in infile:
        direction, steps = parse_line(line.strip())
        for _ in range(steps):
            head_pos = move_head(direction, head_pos)
            tail_pos = move_tail(tail_pos, head_pos)
            visited.add(tail_pos)


print(f"Part 1: The tail visited {len(visited)} positions")

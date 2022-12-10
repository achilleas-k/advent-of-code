import sys
from typing import List, Tuple


fname = sys.argv[1]

def read_instruction(line: str) -> Tuple[int, int]:
    """
    Returns the number of cycles the instruction will take and the value diff to apply at the end.
    """
    if line == "noop":
        return 1, 0

    parts = line.split(" ")
    if len(parts) != 2:
        raise ValueError(f"invalid instruction line: {line}")

    instr, value = parts
    if instr == "addx":
        return 2, int(value)

    raise ValueError(f"invalid instruction {instr}")


cycle = 0
reg = 1
signal_strengths: List[int] = []

stop = 220

with open(fname, encoding="utf-8") as infile:
    for line in infile:
        cycles, value = read_instruction(line.strip())
        for cc in range(cycles):
            cycle += 1
            if (cycle + 20) // 40 > len(signal_strengths):
                # we crossed an interesting cycle: save the current strength at that cycle before updating the register
                signal_strengths.append(cycle * reg)

        if cycle >= stop:
            break

        # update register at the end of the instruction's cycles
        reg += value

print("Signal strenghts")
print(", ".join(str(ss) for ss in signal_strengths))
print(f"Sum: {sum(signal_strengths)}")

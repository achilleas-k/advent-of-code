import re
import sys

from typing import Any, List, Tuple, Dict


fname = sys.argv[1]

Monkey = Dict[str, Any]

monkey_re = re.compile(r"Monkey (?P<monkey>[0-9]+):")


def set_monkey(line: str) -> int:
    matches = monkey_re.match(line)
    if matches:
        return int(matches["monkey"])

    raise ValueError(f"set_monkey: couldn't parse line: {line}")


def set_items(line: str, monkey: Monkey):
    prefix = "Starting items: "
    items = [int(item) for item in line.strip()[len(prefix):].split(", ")]
    monkey["items"] = items


def set_operation(line: str, monkey: Monkey):
    prefix = "Operation: new = "
    monkey["operation"] = line.strip()[len(prefix):]


def set_test(line: str, monkey: Monkey):
    prefix = "Test: divisible by "
    monkey["test"] = {}
    monkey["test"]["condition"] = int(line.strip()[len(prefix):])


def set_true_action(line: str, monkey: Monkey):
    prefix = "If true: throw to monkey "
    monkey["test"][True] = int(line.strip()[len(prefix):])


def set_false_action(line: str, monkey: Monkey):
    prefix = "If false: throw to monkey "
    monkey["test"][False] = int(line.strip()[len(prefix):])


monkeys: Dict[int, Monkey] = {}
monkey_num = -1
with open(fname, encoding="utf-8") as infile:
    for line in infile:
        if line.startswith("Monkey"):
            monkey_num = set_monkey(line)
            monkeys[monkey_num] = {}
        elif line.strip().startswith("Starting items:"):
            set_items(line, monkeys[monkey_num])
        elif line.strip().startswith("Operation:"):
            set_operation(line, monkeys[monkey_num])
        elif line.strip().startswith("Test:"):
            set_test(line, monkeys[monkey_num])
        elif line.strip().startswith("If true"):
            set_true_action(line, monkeys[monkey_num])
        elif line.strip().startswith("If false"):
            set_false_action(line, monkeys[monkey_num])

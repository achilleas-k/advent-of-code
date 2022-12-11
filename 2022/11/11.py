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


def print_monkey_items(monkeys: Dict[int, Monkey]):
    for number, monkey in monkeys.items():
        print(f"Monkey {number}: {', '.join(str(item) for item in monkey['items'])}")


def update_worry(operation: str, value: int) -> int:
    operation = operation.replace("old", str(value))
    return eval(operation)  # naughty


def run_action(monkeys: Dict[int, Monkey], mnum: int):
    monkey = monkeys[mnum]
    for item in monkey["items"]:
        # update the worry value
        new_val = update_worry(monkey["operation"], item) // 3
        # get recipient monkey number based on test condition
        rec_num = monkey["test"][new_val % monkey["test"]["condition"] == 0]
        monkeys[rec_num]["items"].append(new_val)

    # monkey's done throwing: reset items
    monkeys[mnum]["items"] = []


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


nrounds = 20
if len(sys.argv) == 3:
    nrounds = int(sys.argv[2])

action_counts: Dict[int, int] = {}
for rnd in range(nrounds):
    for num in sorted(monkeys.keys()):  # keys should be ordered from creation, but sort them anyway
        # add the number of current items to the action count for the given monkey
        action_count = action_counts.get(num, 0)
        action_counts[num] = len(monkeys[num]["items"]) + action_count
        run_action(monkeys, num)

print_monkey_items(monkeys)
print()

print("Action counts")
for num, count in action_counts.items():
    print(f"Monkey {num} performed {count} actions")

top_actions = sorted(action_counts.values(), reverse=True)
monkey_business = top_actions[0] * top_actions[1]
print(f"Monkey business level: {monkey_business}")

import sys


symbols = {
    "opponent": {
        "A": "Rock", "B": "Paper", "C": "Scissors",
    },
    "me": {
        "X": "Rock", "Y": "Paper", "Z": "Scissors",
    }
}

win = 6
draw = 3
loss = 0


# static rule map
rules = {
    "A": {
        "A": draw,
        "B": win,
        "C": loss,
    },
    "B": {
        "A": loss,
        "B": draw,
        "C": win,
    },
    "C": {
        "A": win,
        "B": loss,
        "C": draw,
    }
}


points = {"A": 1, "B": 2, "C": 3}


def play_p1(me: str) -> str:
    """
    Decide what to play: part 1
    """
    if me == "X":
        return "A"
    if me == "Y":
        return "B"
    if me == "Z":
        return "C"
    raise ValueError(f"Unknown value {me}")


def calc_round_score_p1(opponent: str, me: str) -> int:
    # base shape score + outcome score
    me = play_p1(me)
    return points[me] + rules[opponent][me]


total_score = 0
fname = sys.argv[1]
print(f"Using data from {fname}")
with open(fname, encoding="utf-8") as infile:
    for idx, line in enumerate(infile):
        opponent, me = line.strip().split(" ", 2)
        round_score = calc_round_score_p1(opponent, me)
        print(f"Round {idx+1}: {round_score}")
        total_score += round_score

print(f"Total: {total_score}")

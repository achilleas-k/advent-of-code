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
rules_p1 = {
    "A": {
        "X": draw,
        "Y": win,
        "Z": loss,
    },
    "B": {
        "X": loss,
        "Y": draw,
        "Z": win,
    },
    "C": {
        "X": win,
        "Y": loss,
        "Z": draw,
    }
}

points = {"X": 1, "Y": 2, "Z": 3}


def calc_round_score(opponent: str, me: str) -> int:
    # base shape score + outcome score
    return points[me] + rules_p1[opponent][me]


total_score = 0
fname = sys.argv[1]
print(f"Using data from {fname}")
with open(fname, encoding="utf-8") as infile:
    for idx, line in enumerate(infile):
        opponent, me = line.strip().split(" ", 2)
        round_score = calc_round_score(opponent, me)
        print(f"Round {idx+1}: {round_score}")
        total_score += round_score

print(f"Total: {total_score}")

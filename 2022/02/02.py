import sys


points = {"A": 1, "B": 2, "C": 3}


def calc_score(opponent: str, me: str) -> int:
    me_pts = points[me]
    wld = (ord(opponent) - ord(me)) % 3
    if wld == 0:  # draw
        return 3 + me_pts

    if wld == 1:  # loss
        return 0 + me_pts

    if wld == 2:  # win
        return 6 + me_pts

    raise ValueError(f"WAT: {str(wld)}")


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

    raise ValueError(f"Unknown play value {me}")


def play_p2(opponent: str, outcome: str) -> str:
    """
    Decide what to play: part 2
    """
    if outcome == "Y":
        # draw: play the same
        return opponent

    opponent_idx = "ABC".index(opponent)

    if outcome == "Z":
        # win: idx+1
        return "ABC"[(opponent_idx + 1) % 3]

    if outcome == "X":
        # lose: idx - 1
        return "ABC"[(opponent_idx - 1) % 3]

    raise ValueError(f"Unknown opponent value {opponent}")


def calc_round_score_p1(opponent: str, me: str) -> int:
    # base shape score + outcome score
    me = play_p1(me)
    return calc_score(opponent, me)


def calc_round_score_p2(opponent: str, me: str) -> int:
    # base shape score + outcome score
    me = play_p2(opponent, me)
    return calc_score(opponent, me)


total_score = 0
fname = sys.argv[1]
print(f"Using data from {fname}")
with open(fname, encoding="utf-8") as infile:
    for idx, line in enumerate(infile):
        opponent, me = line.strip().split(" ", 2)
        round_score = calc_round_score_p1(opponent, me)
        # print(f"Round {idx+1}: {round_score}")
        total_score += round_score


print(f"Total (part 1): {total_score}")

total_score = 0
with open(fname, encoding="utf-8") as infile:
    for idx, line in enumerate(infile):
        opponent, me = line.strip().split(" ", 2)
        round_score = calc_round_score_p2(opponent, me)
        # print(f"Round {idx+1}: {round_score}")
        total_score += round_score


print(f"Total (part 2): {total_score}")

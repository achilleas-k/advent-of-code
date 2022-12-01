cur_sum = 0
max_sum = 0
sums = []

with open("./input.txt", encoding="utf-8") as infile:
    for line in infile:
        line = line.strip()
        if line == "":
            sums.append(cur_sum)
            max_sum = max(cur_sum, max_sum)
            cur_sum = 0
        else:
            cur_sum += int(line)

print(max_sum)

top3 = sorted(sums, reverse=True)[:3]
print(top3, sum(top3))

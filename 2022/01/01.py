cur_sum = 0
sums = []

with open("./input.txt", encoding="utf-8") as infile:
    for line in infile:
        line = line.strip()
        if line == "":
            sums.append(cur_sum)
            cur_sum = 0
        else:
            cur_sum += int(line)
    sums.append(cur_sum)  # last elf


sums = sorted(sums, reverse=True)

print(f"Max: {sums[0]}")
top3 = sums[:3]
print(f"top3: {top3}: {sum(top3)}")

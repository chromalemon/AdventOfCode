ids = []
ids_left = []
ids_right = []
total = 0
with open("input.txt", "r") as f:
    for line in f:
        ids.append(line.strip("\n"))
    for row in ids:
        empty = row.index("   ")
        ids_left.append(row[0:empty])
        ids_right.append(row[empty+1:])
    s_left = sorted(ids_left)
    s_right = sorted(ids_right)
    for i in range(len(s_left)):
        diff = int(s_left[i]) - int(s_right[i])
        diff = abs(diff)
        total += diff
    print(total)
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
    for left_item in s_left:
        times = 0
        for right_item in s_right:
            if int(left_item) == int(right_item):
                times += 1
        total += int(times)*int(left_item)
    print(total)
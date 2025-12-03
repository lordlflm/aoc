import sys

current = 50
target = 0
target_cnt = 0

lines = []
with open(sys.argv[1], "r") as f:
    lines = f.readlines()

for line in lines:
    op = line[0]
    arg = int(line[1:])

    # Left
    if op == "L":
        current = (current - arg) % 100
    # Right
    else:
        current = (current + arg) % 100

    if current == target:
        target_cnt += 1

# 1123
print(target_cnt)


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
        if arg >= current:
            if current != 0:
                target_cnt += 1
            target_cnt += (arg - current) // 100
        current = (current - arg) % 100
    # Right
    else:
        if arg >= 100 - current:
            target_cnt += 1 + ((arg - (100 - current)) // 100)
        current = (current + arg) % 100

# 6695
print(target_cnt)


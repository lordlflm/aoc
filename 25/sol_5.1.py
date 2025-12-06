import sys

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

i = lines.index('\n')
ranges = [
    (int(r.strip().split('-')[0]), int(r.strip().split('-')[1])) 
    for r in lines[:i]
]
available = [int(avail) for avail in lines[i+1:]]

fresh_cnt = 0
for id in available:
    is_fresh = False
    for r in ranges:
        if id in range(r[0], r[1] + 1):
            is_fresh = True
            break
    if is_fresh:
        fresh_cnt += 1

print(fresh_cnt)

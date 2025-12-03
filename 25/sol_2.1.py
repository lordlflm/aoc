import sys
import re

with open(sys.argv[1], 'r') as file:
    input = file.readlines()[0].strip()

ranges = [(range.split('-')[0], range.split('-')[1]) for range in input.split(',')]

res = 0
for r in ranges:
    for id in range(int(r[0]), int(r[1]) + 1):
        # check for ids that are made of a sequence repeated twice
        str_id = str(id)
        match = re.match(r'^(\d+)(\1)$', str_id)
        if match is not None:
            res += id

print(res)

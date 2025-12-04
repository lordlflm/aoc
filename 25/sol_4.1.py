import sys

with open(sys.argv[1], "r") as f:
    lines = [line.strip() for line in f.readlines()]

def char_to_int(c):
    if c == '.':
        return 0
    elif c == '@':
        return 1
    else:
        raise Exception

padded_grid = [[0 for _ in range(len(lines[0]) + 2)]]
for line in lines:
    int_line = [0]
    int_line += map(char_to_int, list(line))
    int_line.append(0)
    padded_grid.append(int_line)
padded_grid.append([0 for _ in range(len(lines[0]) + 2)])

round_accessible_roll_of_paper_cnt = 0
for row_idx in range(1, len(padded_grid) - 1):
    for col_idx in range(1, len(padded_grid[0]) - 1):
        if padded_grid[row_idx][col_idx] == 0:
            continue
        
        adj_roll_of_paper_cnt = 0
        for i in range(row_idx - 1, row_idx + 2):
            for j in range(col_idx - 1, col_idx + 2):
                adj_roll_of_paper_cnt += padded_grid[i][j]

        if adj_roll_of_paper_cnt <= 4:
            round_accessible_roll_of_paper_cnt += 1

print(round_accessible_roll_of_paper_cnt)



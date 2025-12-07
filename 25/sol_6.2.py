import sys

operators = []
char_matrix = []
with open(sys.argv[1], "r") as f:
    row = []
    while True:
        r = f.read(1)
        if not r:
            operators = [e for e in row if e != " "]
            break

        if r == "\n":
            char_matrix.append(row)
            row = []
            r = f.read(1)

        row.append(r)


problems = []
row = []
for j in range(len(char_matrix[0])):
    int_str = ''
    for i in range(len(char_matrix)):
        int_str += char_matrix[i][j]

    if int_str == " " * len(char_matrix):
        problems.append(row)
        row = []
        continue
    row.append(int(int_str))
problems.append(row)

res = []
for i in range(len(problems)):
    match operators[i]:
        case '*':
            tmp = 1
            for item in problems[i]:
                tmp *= item
            res.append(tmp)
        case '+':
            res.append(sum(problems[i]))

print(sum(res))
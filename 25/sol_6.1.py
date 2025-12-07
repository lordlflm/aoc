import sys

with open(sys.argv[1], "r") as f:
    problems = [ [e for e in line.strip().split(' ') if e != ''] for line in f.readlines()]

operators = problems[-1]
res = list(map(lambda x: int(x), problems[0]))
problems = problems[1:-1]

for i in range(len(problems)):
    for j in range(len(problems[0])):
        match operators[j]:
            case '+':
                res[j] += int(problems[i][j])
            case '*':
                res[j] *= int(problems[i][j])

print(sum(res))
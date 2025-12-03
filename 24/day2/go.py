reports = []

with open('list1.txt', 'r') as f:
    line = f.readline()
    while line:
        levels = list(map(int, line.split()))
        reports.append(levels)
        line = f.readline()
        
res = 0

def is_valid(report):
    is_increasing = None
    for i in range(len(report)-1):
        # check de croissance/decroissance
        if report[i] - report[i+1] > 0 :
            new_is_inscreasing = True
        elif report[i] - report[i+1] < 0:
            new_is_inscreasing = False
        else:
            break
        if is_increasing == None:
            is_increasing = new_is_inscreasing
        if is_increasing != new_is_inscreasing:
            break
        
        # check d'ecart
        if abs(report[i] - report[i+1]) < 1 or abs(report[i] - report[i+1]) > 3:
            break
        
        if i == len(report)-2:
            return True
        
    return False
        
for report in reports:
    if is_valid(report):
        res += 1
    else:
        for i in range(len(report)):
            tmp = report[:]
            tmp.pop(i)
            print(report)
            print(tmp)
            if is_valid(tmp):
                res += 1
                break

print(res)
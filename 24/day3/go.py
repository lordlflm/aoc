import re

with open('list1.txt', 'r') as f:
    t = f.read()

l = []

while True:
    match = re.search(r'(mul\([1-9]{1}[0-9]{0,2},[1-9]{1}[0-9]{0,2}\))|(do\(\))|(don\'t\(\))', t)
    
    if match is None:
        break
    
    l.append(t[match.start(): match.end()])
    t = t[match.end():]

# print(l)

# if 'don\'t()' in l:
#     print('YERRRRR')

r = 0
dont_flag = False
for item in l:
    if item == 'don\'t()':
        dont_flag = True
    elif item == 'do()':
        dont_flag = False
    elif not dont_flag:  
        s = item[4:-1]
        s = s.split(',')
        r += int(s[0]) * int(s[1])
    
print(r)
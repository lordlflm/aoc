l_list = []
r_list = []

with open('list1.txt', 'r') as f:
    numbers = f.readline()
    while numbers:
        l, r = numbers.split()
        l_list.append(int(l))
        r_list.append(int(r))
        numbers = f.readline()
        
# l_list.sort()
# r_list.sort()

reponse = 0
occurrences = {}

for i in range(len(l_list)):
    if l_list[i] not in occurrences:
        occurrence = 0
        for j in range(len(r_list)):
            if l_list[i] == r_list[j]:
                occurrence += 1
        occurrences[l_list[i]] = occurrence
        
    reponse += l_list[i] * occurrences[l_list[i]]
        

# if len(r_list) != len(l_list):
#     print("PROBLEM")
    
# for i in range(len(l_list)):
#     reponse += abs(l_list[i]-r_list[i])
    
print(reponse)
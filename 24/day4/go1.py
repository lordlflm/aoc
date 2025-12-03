matrix = []

with open('list.txt', 'r') as f:
    t = f.readline()
    while t:
        matrix.append(t)
        t = f.readline()
    
# print(matrix)

r = 0

for i, line in enumerate(matrix):
    for j, c in enumerate(line):
        if c == 'X':
            #right
            if line[j: j+4] == 'XMAS':
                r+=1
            # left
            if line[j-3:j+1] == 'SAMX':
                r+=1
                
            # nord
            if i > 2:
                # diag west
                if matrix[i-1][j-1] == 'M' and matrix[i-2][j-2] == 'A' and matrix[i-3][j-3] == 'S':
                    r+=1
                    
                # diag east
                if matrix[i-1][j+1] == 'M' and matrix[i-2][j+2] == 'A' and matrix[i-3][j+3] == 'S':
                    r+=1
                    
                # straight
                if matrix[i-1][j] == 'M' and matrix[i-2][j] == 'A' and matrix[i-3][j] == 'S':
                    r+=1
                
            # south
            if i < len(matrix) - 3:
                # diag west
                if matrix[i+1][j-1] == 'M' and matrix[i+2][j-2] == 'A' and matrix[i+3][j-3] == 'S':
                    r+=1
                    
                # diag east
                if matrix[i+1][j+1] == 'M' and matrix[i+2][j+2] == 'A' and matrix[i+3][j+3] == 'S':
                    r+=1
            
                # straight
                if matrix[i+1][j] == 'M' and matrix[i+2][j] == 'A' and matrix[i+3][j] == 'S':
                    r+=1
            
            
print(r)
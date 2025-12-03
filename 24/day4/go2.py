matrix = []

with open('list.txt', 'r') as f:
    t = f.readline()
    while t:
        matrix.append(t)
        t = f.readline()
    
for i, line in enumerate(matrix):
    if i != len(matrix) - 1:
        line = line[:-1]
        matrix[i] = line
        
# print(matrix)

def is_south_west_mas(i, j):
    global matrix
    if i < len(matrix) - 2 and j > 1:
        if matrix[i][j] == 'M' and matrix[i+1][j-1] == 'A' and matrix[i+2][j-2] == 'S':
            return True
    
    return False

def is_south_east_mas(i, j):
    global matrix
    if i < len(matrix) - 2 and j < len(matrix[0]) - 2:
        if matrix[i][j] == 'M' and matrix[i+1][j+1] == 'A' and matrix[i+2][j+2] == 'S':
            return True
    
    return False

def is_north_west_mas(i, j):
    global matrix
    if i > 1 and j > 1:
        if matrix[i][j] == 'M' and matrix[i-1][j-1] == 'A' and matrix[i-2][j-2] == 'S':
            return True
    
    return False

def is_north_east_mas(i, j):
    global matrix
    if i > 1 and j < len(matrix[0]) - 2:
        if matrix[i][j] == 'M' and matrix[i-1][j+1] == 'A' and matrix[i-2][j+2] == 'S':
            return True
    
    return False

r = 0
visited_x_middles = []

for i, line in enumerate(matrix):
    for j, c in enumerate(line):
        # print(c)
        if c == 'M':
            if (i+1,j-1) not in visited_x_middles:
                if is_south_west_mas(i, j) and is_south_east_mas(i, j-2):
                    print('SW-SE')
                    print((i+1,j-1))
                    visited_x_middles.append((i+1,j-1))
                    r+=1
                    
                if is_south_west_mas(i, j) and is_north_west_mas(i+2, j):
                    print('SW-NW')
                    print((i+1,j-1))
                    visited_x_middles.append((i+1,j-1))
                    r+=1
            if (i-1,j+1) not in visited_x_middles:    
                if is_north_east_mas(i, j) and is_north_west_mas(i, j+2):
                    
                    print('NE-NW')
                    print((i-1,j+1))
                    visited_x_middles.append((i-1,j+1))
                    r+=1
                    
                if is_north_east_mas(i, j) and is_south_east_mas(i-2, j):
                    print('NE-SE')
                    print((i-1,j+1))
                    visited_x_middles.append((i-1,j+1))
                    r+=1
                    
             
print(visited_x_middles)            
    
print(r)
            
matrix = []
for i in range(5):
    matrix.append(list(map(int,input().split())))
 
moves = 0
for row in matrix :
    if 1 in row :
        moves += abs(2-matrix.index(row)) + abs(2-row.index(1))
        break
print(moves)
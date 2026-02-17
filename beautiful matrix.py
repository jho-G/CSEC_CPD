matrix=[]
for _ in range(5):
    row=list(map(int,input().split()))
    matrix.append(row)

for r in range(5):
    for c in range(5):
        if matrix[r][c]==1:
            row_1,col_1=r,c
            break

moves=abs(2-row_1)+abs(2-col_1)
print(moves)

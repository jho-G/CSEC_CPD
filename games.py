x=int(input())
c=0
m=[]
for i in range(x):
    t=[int(i) for i in input().split()]
    m.append(t)
for i in range(x):
    for j in range(x):
        if i!=j and m[i][0]==m[j][1]:
            c+=1
print(c)

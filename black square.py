x=[int(i) for i in input().split()]
y=input()
m=list(y)
c=0
for i in range(len(m)):
    if m[i]=='1':
        c+=x[0]
    elif m[i]=='2':
        c+=x[1]
    elif m[i]=='3':
        c+=x[2]
    else:
        c+=x[3]
print(c)

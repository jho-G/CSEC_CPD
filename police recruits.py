n=int(input())
a=list(map(int, input().split()))
c=0
po=0
for i in range (n):
    if a[i]>0:
        po+=a[i]
    if a[i]==-1:
        if po>0:
            po-=1
        else:
            c+=1
print(c)

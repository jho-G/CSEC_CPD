n=int(input())

first=input()
count=1

for _ in range(n-1):
    next=input()
    if next!=first:
        count+=1
    
    first=next
print(count)
    

values=list(map(int,input()))
strips=input()
count=0

for i in strips:
    count+=values[int(i)-1]

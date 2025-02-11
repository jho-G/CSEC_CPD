n = int(input())
a = []
count = 0
first_magnet = input()
a.append(first_magnet)
for i in range(1,n):
    magnet = input()
    if a[i-1] == magnet:
        a.append(magnet)
    else:
        count = count + 1
        a.append(magnet)
print(count+1)

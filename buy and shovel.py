a = list(map(int, input().split()))
reached = False
n = 1
while not reached:
    if (a[0] * n)%10 - a[1] == 0:
        reached = True
    elif (a[0] * n)%10 == 0:
        reached = True
    else:
        n += 1

print(n)

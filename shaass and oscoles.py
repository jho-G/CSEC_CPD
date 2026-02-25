n = int(input())
a = list(map(int, input().split()))
m = int(input())

for _ in range(m):
    x, y = map(int, input().split())
    
    x -= 1  
    
    left_birds = y - 1
    right_birds = a[x] - y
    
    if x > 0:
        a[x - 1] += left_birds
    
    if x < n - 1:
        a[x + 1] += right_birds
    
    a[x] = 0

for birds in a:
    print(birds)

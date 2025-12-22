t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input()

    last_one = -10**9   
    protect = 0

    for i in range(n):
        if s[i] == '1':
            
            if i - last_one >= k:
                protect += 1      
                last_one = i      
            else:
                last_one = i      

    print(protect)

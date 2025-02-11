s = input()
shortest = 0
start = 'a'

for i in range(len(s)):
    forward = abs(ord(s[i])-ord(start))
    reverse = 26 - forward
    if forward > reverse:
        shortest += reverse
    else:
        shortest += forward
    start = s[i]
print(shortest)

n = int(input())
s = list(input())
i = 1
min_no = 0
while i < len(s):
    if s[i-1] == s[i]:
        s.pop(i-1)
        min_no +=1
    else:
       i += 1
print(min_no)

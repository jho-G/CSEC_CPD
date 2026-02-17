s1=input().lower()
s2=input().lower()
for i in range(len(s1)):
    if s1[i]<s2[i]:
        print(-1)
        break
    elif s1[i]>s2[i]:
        print(1)
        break
else:
        print(0)
        




    

n=input()

current="a"
count=0

for ch in n:
    diff=abs(ord(ch)-ord(current))
    moves+=min(diff,26-diff)
    current=ch
print(count)

First = input()
second = input()
First = First.lower()
second = second.lower()
if First > second:
    print(1)
if second > First:
    print(-1)
if First == second:
    print(0)

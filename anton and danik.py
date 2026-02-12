num_of_game=int(input())
str1=input().strip()
count_A=str1.count('A')
count_D=str1.count('D')
if count_A>count_D:
    print("Anton")
elif count_D>count_A:
    print("Danik")
else:
    print("Friendship")

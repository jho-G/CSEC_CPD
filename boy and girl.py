user_name = input()
user_list = list(user_name)
n = len(user_list)
user_list.sort()
count = 0
for i in range(n-1):
    if user_list[i] == user_list[i+1]:
        count = count
    else:
        count = count + 1
count = count + 1
if count % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")

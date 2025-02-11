n = int(input())
n_list = list(map(int, input().split()))
count_s = 0
count_d = 0

for i in range(n):
    if i % 2 == 0:
        if n_list[0] < n_list[-1]:
            count_s = count_s + n_list[-1]
            n_list.pop()
        else:
            count_s = count_s + n_list[0]
            n_list.pop(0)
    else: 
        if n_list[0] < n_list[-1]:
            count_d = count_d + n_list[-1]
            n_list.pop()
        else:
            count_d = count_d + n_list[0]
            n_list.pop(0)

print(count_s, count_d)

s = input().strip()
t = input().strip()

position = 0

for char in t:
    if position < len(s) and char == s[position]:
        position += 1

print(position + 1)

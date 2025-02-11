word = input()
upper = []
lower = []
for i in range(len(word)):
    if word[i].isupper():
        upper.append(word[i])
    else:
        lower.append(word[i])

if len(upper) > len(lower):
    print(word.upper())
else:
    print(word.lower())

n, h=map(int, input().split())
a=list(map(int, input().split()))
print(sum(2 if x >h else i for x in a))

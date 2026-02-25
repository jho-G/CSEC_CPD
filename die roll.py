import math

Y, W = map(int, input().split())

m = max(Y, W)

favorable = 6 - m + 1
total = 6

g = math.gcd(favorable, total)

print(f"{favorable//g}/{total//g}")

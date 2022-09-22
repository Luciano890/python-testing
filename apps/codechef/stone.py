"""Stone Problem"""
from sys import stdin

rl = stdin.readline

a, k = map(int, rl().split())
n = list(map(int, rl().split()))

mx = max(n)
res = list(map(lambda x: mx - x, n))

if k == 0:
    print(*n)
elif k&1:
    print(*res)
else:
    mx = max(res)
    print(*list(map(lambda x: mx - x, res)))

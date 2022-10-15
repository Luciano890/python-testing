"""..."""
from sys import stdin

rl = stdin.readline

for _ in range(int(rl())):
    n = input()
    colors = list(map(int, rl().split()))
    if len(set(colors)) == len(colors):
        print(0)

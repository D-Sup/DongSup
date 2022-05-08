# baekjoon 3052
import sys
input = sys.stdin.readline
N, M = [], []
r = 0
for _ in range(10):
    l = int(input())
    N.append(l)
for k in range(10):
    M.append(N[k] % 42)
print(len(set(M)))

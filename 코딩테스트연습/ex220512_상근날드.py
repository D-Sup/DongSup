# baekjoon 5543
import sys
input = sys.stdin.readline
N, M= [], []
for _ in range(3):
    l = int(input())
    N.append(l)
for _ in range(2):
    p = int(input())
    M.append(p)
print(min(N)+min(M)-50)

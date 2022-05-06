# 백준 2460번
import sys
S = 0
L = []
for i in range(10):
    N, M = map(int,sys.stdin.readline().split())
    S -= N
    S += M
    L.append(S)
print(max(L))
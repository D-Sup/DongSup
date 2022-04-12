# 백준 9085번
import sys
T = int(sys.stdin.readline())
E = []
for _ in range(T):
    N = int(sys.stdin.readline())
    S = list(map(int,sys.stdin.readline().split()))
    if len(S) > N or len(S) < N:
        break
    E.append(sum(S))
for i in range(T):
    print(E[i])
# 백준 2577번
import sys
N = []
V, r = 1, 0
for _ in range(3):
    L = int(sys.stdin.readline())
    N.append(L)
for i in range(len(N)):
    V*=N[i]
V = list(map(int,str(V)))
for p in range(10):
    for q in range(len(V)):
        if V[q] == p:
            r+=1
    print(r)
    r=0 
import imp


import sys
T = int(sys.stdin.readline())
for _ in range(T):
    V, E = map(int,sys.stdin.readline().split())
    M = -((V - E) - 2)
    print(M)
    
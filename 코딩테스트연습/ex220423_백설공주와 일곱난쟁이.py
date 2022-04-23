# 백준 3040번
import sys
N = []
for _ in range(9):
    N.append(int(sys.stdin.readline()))
V = sum(N) - 100
for i in range(len(N)):
    for j in range(len(N)):
        if V == N[j] + N[i] and len(N) == 9:
            A, B = j, i
del(N[A])
del(N[B-1])
for X in range(len(N)):
    print(N[X])
            
            
            
 
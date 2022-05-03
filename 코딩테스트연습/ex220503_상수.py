# 백준 2908번
import sys
A, B = sys.stdin.readline().split()
x, y = str(A), str(B)
C, D = [], []
for i in range(len(x)-1,-1,-1):
    C.append(x[i])
for j in range(len(y)-1,-1,-1):
    D.append(y[j])
F = int("".join(C))
G = int("".join(D))
if F > G:
    print(F)
else:
    print(G)

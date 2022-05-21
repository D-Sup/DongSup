# baekjoon 2902
import sys
input = sys.stdin.readline
M = []
N = list(input())
del(N[-1])
for i in N:
    if ord(i) == 45:
        M.append(N[N.index(i)+1])
        del(N[N.index(i)])
print(N[0],end='')
for j in M:
    print(j,end='')
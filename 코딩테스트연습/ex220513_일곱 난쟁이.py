# baekjoon 2309 
import sys
input = sys.stdin.readline
N = []
for _ in range(9):
    N.append(int(input()))
l = sum(N) - 100
for i in range(9):
    for j in range(9):
        if N[i]+N[j] == l:
            a = N.index(N[i])
            b = N.index(N[j])
if a > b:
    del(N[a])
    del(N[b])
else:
    del(N[b])
    del(N[a])
N.sort()
for k in range(7):
    print(N[k])
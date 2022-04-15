# 백준 2455번
import sys
N = int(sys.stdin.readline())
M = list(map(int,sys.stdin.readline().split()))
S, H = 0, 0
for i in range(N):
    if M[i] != 0:
        S += 1
        H += S
    else:
        S = 0
print(H)
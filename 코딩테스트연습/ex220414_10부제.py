# 백준 10797번
import sys
s = 0
N = int(sys.stdin.readline())
M = list(map(int,sys.stdin.readline().split()))
for i in range(len(M)):
    if M[i] == N :
        s += 1
print(s)
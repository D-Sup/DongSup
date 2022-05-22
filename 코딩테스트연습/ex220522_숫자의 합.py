# baekjoon 11720
import sys
input = sys.stdin.readline
H = 0
N = int(input())
M = list(map(str,input()))
del(M[-1])
for i in M:
    if len(M) == N:
        H += int(i)
print(H)
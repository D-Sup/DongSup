# baekjoon 2750
import sys
input = sys.stdin.readline
N = int(input())
T = []
for _ in range(N):
    T.append(int(input()))
T.sort()
for i in range(N):
    print(T[i])

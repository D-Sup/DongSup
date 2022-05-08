# baekjoon 1292
import sys
input = sys.stdin.readline
l = []
N, M = map(int,input().split())
for i in range(N+1,M):
    l.append(i)
print(sum(l))
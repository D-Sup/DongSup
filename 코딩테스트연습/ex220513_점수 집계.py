# baekjoon 9076
import sys
input = sys.stdin.readline
N = int(input())
for _ in range(N):
    M = list(map(int,input().split()))
    del(M[M.index(min(M))])
    del(M[M.index(max(M))])
    if max(M) - min(M) >= 4:
        print('KIN')
    else:
        print(sum(M))
    del(M)
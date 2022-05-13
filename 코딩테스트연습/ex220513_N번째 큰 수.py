# baekjoon 2693
import sys
input = sys.stdin.readline
N = int(input())
for _ in range(N):
    M = list(map(int,input().split()))
    M = sorted(M, reverse=True)
    print(M[2])
    del(M)
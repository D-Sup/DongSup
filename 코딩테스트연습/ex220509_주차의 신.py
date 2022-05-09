# baekjoon 5054
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    m = list(map(int,input().split()))
    U = (sorted(m))
    print((U[-1]-U[0])*2)
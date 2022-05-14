# baekjoon 3058
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    M = []
    N = list(map(int,input().split()))
    for i in range(len(N)):
        if N[i]%2==0:
            M.append(N[i])
    print(sum(M),min(M))
    del(N,M)
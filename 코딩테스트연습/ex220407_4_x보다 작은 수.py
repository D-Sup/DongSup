import sys
N, X = map(int,sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))
for i in range(N):
    if X > A[i]:
        print(A[i],end=' ')

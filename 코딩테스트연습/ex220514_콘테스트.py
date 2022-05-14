# baekjoon 5576
import sys
input = sys.stdin.readline
R = []
for _ in range(2):
    N, M = [], []
    for _ in range(10):
        N.append(int(input()))
    N = sorted(N, reverse=True)
    for i in range(3):
        M.append(N[i])
    R.append(sum(M))
    del(N,M)
print(R[0],R[1],sep=' ')


    
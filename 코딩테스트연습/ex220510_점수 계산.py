# baekjoon 2822
import sys
input = sys.stdin.readline
N , K = [], []
S = 0
for _ in range(8):
    N.append(int(input()))
    D = sorted(N, reverse=True)
for i in range(5):
    S += D[i]
    K.append(N.index(D[i])+1)
    K.sort()
print(S)
for j in range(len(K)):
    print(K[j], end = ' ')

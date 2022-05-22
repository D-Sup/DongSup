# baekjoon 4458
import sys
input = sys.stdin.readline
N = int(input())
M = []
for _ in range(N):
    M.append(list(input()))
for i in range(len(M)):
    if ord(M[i][0]) > 96:
        M[i][0] = chr(ord(M[i][0]) - 32)
for q in range(len(M)):
    for w in range(len(M[q])):
        print(M[q][w],end='')
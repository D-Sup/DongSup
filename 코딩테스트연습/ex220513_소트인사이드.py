# baekjoon 1427
import sys
input = sys.stdin.readline
M = []
N = list(str(input()))
del(N[-1])
for i in range(len(N)):
    M.append(int(N[i]))
M.sort(reverse=True)
for j in range(len(M)):
    print(M[j],end='')

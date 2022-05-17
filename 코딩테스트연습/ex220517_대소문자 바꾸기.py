# baekjoon 2744
import sys
input = sys.stdin.readline
M = []
N = list(input())
for i in N:
    if  ord(i) < 91:
        M.append(ord(i)+32)
    else:
        M.append(ord(i)-32)
del(M[-1])
for j in M:
    print(chr(j),end='')

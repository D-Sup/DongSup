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
        
M = []
for _ in range(int(input())):
    M.append(list(map(str, input())))
for i in range(len(M)):
    M[i][0] = M[i][0].upper()
for j in range(len(M)):
    print(*M[j],sep='')
    
# new method
for _ in range(int(input())):
    N = str(input())
    print(N[0].upper() + N[1::])
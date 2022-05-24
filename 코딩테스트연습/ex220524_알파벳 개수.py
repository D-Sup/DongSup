# baekjoon 10808
import sys 
int = sys.stdin.readline
A = 'abcdefghijklmnopqrstuvwxyz'
N = input()
M = [0*len(A) for i in A]
for i in N:
    if i in A:
        M[A.index(i)]+=1
for j in M:
    print(j,end=' ')
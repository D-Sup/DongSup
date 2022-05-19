# baekjoon 5800
import sys
input = sys.stdin.readline
N = int(input())
for i in range(N):
    G = []
    M = list(map(int,input().split()))
    del(M[0])
    M.sort()
    for j in range(len(M)-1):
        G.append(M[j+1]-M[j])
    print('Class' , i+1)
    print('Max', str(max(M))+',' ,'Min', str(min(M))+',' ,'Largest gap' , max(G))
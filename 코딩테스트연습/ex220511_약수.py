# baekjoon 1037
import sys
input = sys.stdin.readline
r = 0
p = 0
V, c = [1], []
N = int(input())
T = list(map(int,input().split()))
for i in range(len(T)):
    V.append(0)
    while V[-1] < 100:
        r += 1
        V.append(T[i] * r)
    r = 0
for j in range(len(V)):
    for p in range(len(T)):
        if max(T) < V[j] and max(T) != V[j] and V[j]%T[p]==0:
            c.append(V[j])
print(max(c, key = c.count))          
                


    
# 백준 10178번
import sys
N = int(sys.stdin.readline())
c, v = [], []
for _ in range(N):
    a, b = map(int,sys.stdin.readline().split())
    c.append(a//b),v.append(a%b)
for i in range(N):
    print('You get' , c[i] , 'piece(s) and your dad gets' , v[i] , 'piece(s).')
# 백준 10952번
n = int(input())
s = []
for _ in range(n):
    a, b = map(int,input().split())
    s.append(a+b)
for i in s:
    print(i)


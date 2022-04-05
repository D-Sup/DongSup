# 백준 2442번
N = int(input())
a, b, c = [], [], []
for _ in range(N):
    x, y = map(int,input().split())
    a.append(x),b.append(y)
    c.append(b[-1] % a[-1])
print(sum(c))
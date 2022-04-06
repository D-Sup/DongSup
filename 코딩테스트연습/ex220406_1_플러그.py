# 백준 2010번
N = int(input())
M = []
for _ in range(N):
    M.append(int(input()))
print(sum(M)-(N-1))
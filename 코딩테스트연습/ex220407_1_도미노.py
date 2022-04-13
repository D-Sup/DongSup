# 백준 2921번
import sys
N = int(sys.stdin.readline())
S = 0
for i in range(N+1):
    for _ in range(i+1):
        S += 1 
print(S*N)

# n = int(input())
# sum = 0
# for i in range(0, n + 1):
#     for j in range(i, n + 1):
#         sum += i + j
# print(sum)
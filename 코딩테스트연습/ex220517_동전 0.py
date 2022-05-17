# baekjoon 11047
import sys
input = sys.stdin.readline
M = []
P = 0
N, K = map(int,input().split())
for _ in range(N):
    M.append(int(input()))
M.sort(reverse=True)
for i in range(len(M)):
    while M[i] <= K:
        K = K - M[i]
        P += 1
print(P)

# import sys
# input = sys.stdin.readline
# M = []
# R, P = 0, 0
# N, K = map(int,input().split())
# M = sorted([int(input()) for _ in range(N)],reverse=True)
# for i in M:
#     if K >= i:
#         R += K//i
#         K %= i
# print(R)

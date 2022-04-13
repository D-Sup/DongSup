# 벡준 2475번
import sys
H = 0
N = list(map(int,sys.stdin.readline().split()))
for i in range(len(N)):
    S = N[i]*N[i]
    H += S
print(H%10)

# N = list(map(int, input().split()))
# R = 0
# for i in N:
#     R += i*i
# print(R % 10)
# baekjoon 3460
import sys
input = sys.stdin.readline
N = int(input())
M = []
while 0 < N:
    K = N % 2 
    M.append(K)
    N = N // 2
for i in range(len(M)):
    if M[i] == 1:
        print(i, end=' ')
print(M)

# T = int(input())

# for _ in range(T):
#     n = bin(int(input()))[2:]
#     for i in range(len(n)):
#         if n[-i - 1] == '1':
#             print(i, end=' ')

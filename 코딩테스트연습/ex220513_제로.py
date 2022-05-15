# baekjoon 10773
import sys
input = sys.stdin.readline
M, D = [], []
N = int(input())
for _ in range(N):
    M.append(int(input()))
for i in range(len(M)):
    if M[i] == 0:
        D.append(i)
for _ in range(len(D)):
    del(M[D[0]-1])
    l = len(D)
    for j in range(len(D)):
        D.append(D[j]-1)
    for k in range(l):
        del(D[0])
    del(M[D[0]])
    del(D[0])
    if len(D) != 0:
        l = len(D)
        for j in range(len(D)):
            D.append(D[j]-1)
        for k in range(l):
            del(D[0])
print(sum(M))

# import sys
# input = sys.stdin.readline
# K = []
# N = int(input())
# for _ in range(N):
#     M = int(input())
#     if M == 0:
#         K.pop()
#     else:
#         K.append(M)
# print(sum(K))


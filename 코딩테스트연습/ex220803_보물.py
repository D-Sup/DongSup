# baekjoon 1026
N = int(input())
A = sorted(list(map(int,input().split())))
B = sorted(list(map(int,input().split())),reverse=True)
print(sum([A[i]*B[i] for i in range(len(A))]))

# N = int(input())
# A = list(map(int,input().split()))
# B = list(map(int,input().split()))
# a = sorted(A)
# b = sorted(B,reverse=True)
# for i in range(len(A)):
#     A[B.index(b[i])]=a[i]
# H = 0
# for j in range(len(A)):
#     H += A[j]*B[j]
# print(H)

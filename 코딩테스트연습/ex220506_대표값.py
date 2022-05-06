# baekjoon 2592
import sys
input = sys.stdin.readline
N = [int(input()) for i in range(10)]
print(sum(N)//10)
print(max(N, key = N.count))

# import sys
# A = []
# for _ in range(10):
#     N = sys.stdin.readline()
#     A.append(int(N))
# print(sum(A)//10)
# result = [0 for _ in range(len(A))]
# for i in range(len(A)):
#     for j in range(len(A)):
#         if A[i] == A[j]:
#             result[j]+=1
# print(A[result.index(max(result))])


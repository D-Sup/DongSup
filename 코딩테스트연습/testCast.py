# def solution(A,B):
#     C = B.copy()
#     for i in range(len(B)):
#         for j in range(len(B[0])):
#             B[i][j] += A[i][j] 
#     return C
# print(solution([[1,2],[2,3]],[[3,4],[5,6]]))

# import numpy as np
# def solution(A,B):
#     a = np.array(A)
#     b = np.array(B)
#     H = a + b
#     return H.tolist()
# print(solution([[1,2],[2,3]],[[3,4],[5,6]]))

# def solution(A,B):
#     answer = []
#     for a,b in zip(A,B):
#         l = []
#         for c,d in zip(a,b):
#             l.append(c+d)
#         answer.append(l)
#     return answer
# print(solution([[1,2],[2,3]],[[3,4],[5,6]]))

# def solution(A,B):
#     answer = [[c+d for c,d in zip(a,b)] for a,b in zip(A,B)]
#     return answer
# print(solution([[1,2],[2,3]],[[3,4],[5,6]]))
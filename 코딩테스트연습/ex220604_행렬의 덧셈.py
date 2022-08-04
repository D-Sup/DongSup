# programmers 12950
def solution(A,B):
    C = B.copy()
    for i in range(len(B)):
        for j in range(len(B[0])):
            C[i][j] += A[i][j] 
    return C
print(solution([[1,2],[2,3]],[[3,4],[5,6]]))

# new method
# def solution2(arr1, arr2):
#     answer = [[arr1[i][j] + arr2[i][j]
#                for j in range(len(arr1[0]))] for i in range(len(arr1))]
#     return answer
# print(solution2([[1,2],[2,3]],[[3,4],[5,6]]))


# A, B = [[1,2],[2,3]],[[3,4],[5,6]]
# answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A, B)]
# print(answer)
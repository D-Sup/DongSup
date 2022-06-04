# programmers 12950
def solution(A,B):
    C = B.copy()
    for i in range(len(B)):
        for j in range(len(B[0])):
            B[i][j] += A[i][j] 
    return C
print(solution([[1,2],[2,3]],[[3,4],[5,6]]))
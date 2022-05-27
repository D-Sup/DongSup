def sumMatrix(A,B):
    for i in range(len(B)) :
        for j in range(len(B[0])):
           # print(i,j)
            B[i][j] += A[i][j]
           # print(B[i][j])
           # print(B)
           #print("-----")
    return B

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(sumMatrix([[1,2], [2,3]], [[3,4],[5,6]]))

def sumMatrix(A,B):
    answer = []

    for a, b in zip(A, B):
        l = []
        for x, y in zip(a, b):
            l.append(x + y)
        answer.append(l)

    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(sumMatrix([[1,2], [2,3]], [[3,4],[5,6]]))


def sumMatrix(A,B):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(sumMatrix([[1,2], [2,3]], [[3,4],[5,6]]))


def sumMatrix(A,B):
    return [list(map(sum, zip(*x))) for x in zip(A, B)]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(sumMatrix([[1,2], [2,3]], [[3,4],[5,6]]))

import numpy as np
def sumMatrix(A,B):
    A=np.array(A)
    B=np.array(B)
    answer=A+B
    return answer.tolist()

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(sumMatrix([[1,2], [2,3]], [[3,4],[5,6]]))
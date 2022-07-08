from math import sqrt,pow
def solution(n):
    a = sqrt(n)
    return int(pow(a+1,2)) if a > 0 and a%1==0.0 else -1
print(solution(121))

# def solution(n):
#     a = n ** (1/2)
#     return (a+1)**2 if a > 0 and a%1==0.0 else -1
# print(solution(121))
# programmers 12954
def solution(x, n):
    return [x*i for i in range(1,n+1)] 
print(solution(2,5))

# new method
# def solution(x, n):
#     answer = [a for a in range(x, (n+1)*x, x)] if x else [0]*n
#     # = [i*x*x for i in range(n)]
#     return answer
# print(solution(2,5))
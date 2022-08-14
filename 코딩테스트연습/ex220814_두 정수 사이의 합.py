# programmers 12912
def solution(a, b):  
    return sum([i for i in range(a,b+1)]) if a<b else sum([i for i in range(a,b-1,-1)])
print(solution(3,5))

def solution(a, b):
    return sum(range(a,b+1) if a <= b else range(b,a+1))

# ---------------------------------------------------------

# 인자 값만 조건문 돌리기 
def solution(a, b):
    if a > b: a, b = b, a
    return sum(range(a,b+1))
print(solution(3, 5))

# 절대값 활용
def solution(a, b):
    return (abs(a-b)+1)*(a+b)//2
print( solution(3, 5))

# 최솟값 최댓값 활용 
def solution(a, b):
    return sum(range(min(a,b),max(a,b)+1))
print( solution(3, 5))
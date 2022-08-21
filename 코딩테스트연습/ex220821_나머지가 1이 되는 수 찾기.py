# programmers 87389
# 내 풀이 
def solution(n):
    answer = n-1
    for i in range(2,answer+1):
        if answer%i==0:
            return i
print(solution(12))

def solution(n):
    return [i for i in range(1,n+1) if n%i==1][0]
print(solution(12))


# programmers 12928
def solution(n):
    return sum([i for i in range(1,n+1) if n % i == 0])  
print(solution(int(input())))

# def solution(n):
#     return sum(filter(lambda x:n%x==0,range(1,n+1)))
# print(solution(int(input())))

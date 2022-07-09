# programmers 12932
def solution(n):
    R = list(map(int,str(n)))
    R.reverse()
    return R 
print(solution(12345))

# def solution(n):
#     return list(map(int, reversed(str(n))))
# print(solution(12345))

# def solution(n):
#     return [int(i) for i in str(n)][::-1]
# print(solution(12345))

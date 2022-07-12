# programmers 12931
def solution(n):
    # m = list(map(int,str(n)))
    return sum([int(i) for i in str(n)])

print(solution(123))
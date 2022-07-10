# programmers 12933
def solution(n):
    R = [int(i) for i in str(n)]
    R.sort(reverse=True)
    return int("".join(map(str,R)))
print(solution(118372))

# def solution(n):
#     R = list(str(n))
#     R.sort(reverse=True)
#     return int("".join(R))
# print(solution(118372))

# def solution(n):
#     return int("".join(sorted(list(str(n)), reverse=True)))
# print(solution(118372))
# programmers 12947
def solution(n):
    return n%sum(list(map(int, str(n)))) == 0
m = [10,12,11,13]
for i in m:  
    print(solution(i))


# def solution(n):
#     return n % sum([int(c) for c in str(n)]) == 0
# m = [10,12,11,13]
# for i in m:  
#     print(solution(i))


# def solution(n):
#     n = list(map(int, str(n)))
#     m = int("".join(map(str, n)))
#     print(n)
#     if m%sum(n) == 0:
#         return True
#     else:
#         return False
# print(solution(10))
# print(solution(12))
# print(solution(11))
# print(solution(13))


# def solution(n):
#     st = str(n)
#     a = 0
#     for i in range(len(st)):
#         a += int(st[i])
#     return True if n%a == 0 else False
# print(solution(18))


# def solution(n):
#     s=sum([int(i) for i in str(n)])
#     if n%s == 0:
#         return True
#     return False
# print(solution(18))
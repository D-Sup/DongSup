# programmers 12943
def solution(num):
    for i in range(500):
        num = num//2 if num % 2 == 0 else num*3+1
    if num == 1:
        return i+1
    return -1
 
print(solution(626331))

# def solution(num):
#     r = 0
#     while num != 1:
#         if num % 2 == 0:
#             num//=2
#             r+=1
#         else:
#             num=(num*3)+1
#             r+=1
#         if r == 500:
#             return -1
#     return r
# print(solution(626331))

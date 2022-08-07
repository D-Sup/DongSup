# programmers 12921
def solution(n):
    num = set(range(2,n+1))

    for i in range(2,n+1):
        num -= set(range(i*2,n+1,i))
    
    return len(num)

print(solution(10))

# def solution(n):
#     for j in range(2,int(n**0.5)+1):
#         if n%j == 0:
#             return False
#     return True
# L = [10, 5]
# for LL in L:
#     r = 0
#     for i in range(2,LL+1):
#         if solution(i):
#             r+=1
#     print(r)

# programmers 12921
def solution(n):
    num = set(range(2,n+1)) 

    for i in range(2,n+1): 
        print(i)
        num -= set(range(i*2,n+1,i)) 
        print(num)
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

# ==================================================
# def solution(n):
#     return len([i for i in range(2, n + 1) if len([True for j in range(1, i) if i % j == 0]) == True])
# print(solution(10))

# r = 0
# for i in range(2, 10 + 1):
#     L = []
#     for j in range(1, i):
#         if i % j == 0:
#             L.append(True)
#     if len(L) == 1:
#         r += 1
# print(r)
# ==================================================

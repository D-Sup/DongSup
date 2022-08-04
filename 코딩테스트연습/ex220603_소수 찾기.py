# baek1978
k = int(input())
C = 0
M = list(map(int,input().split()))
for i in M:
    if i != 1:
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            C += 1
print(C)

# L = []
# N = int(input())
# M = list(map(int,input().split()))
# for j in M:
#     if j == 1:
#         L.append(j)
#     for i in range(2,j):
#         if j%i == 0:
#             L.append(j)
# L2 = list(set(L))
# M = [k for k in M if k not in L2]
# print(len(M))

# n = int(input())
# nums = list(map(int, input().split(' '))) 
# resCnt = 0 
# for i in nums:
#     cnt = 0 
#     if(i == 1): 
#         continue
#     for j in range(2, i+1):
#         if(i % j == 0):
#             cnt += 1
#     if(cnt == 1):
#         resCnt += 1
# print(resCnt)

# new method
# def s(x):
#     if x == 1:
#         return 0
#     for i in range(2, x):
#         if not (x % i):
#             return 0
#     return 1


# input()
# n = [int(x) for x in input().split()]
# cnt = 0

# for nn in n:
#     if s(nn):
#         cnt += 1

# print(cnt)
# baekjoon 4948
n, m = [], []
while 1:
    n.append(int(input()))
    if n[-1]==0:
        break  
for k in n:    
    c = 0
    for i in range(k+1, (k*2)+1):
        if i == 1: 
            continue
        for j in range(2, int(i** 0.5)+1 ):
            if i%j==0:
                break
        else:
            c += 1
    m.append(c)
del(m[-1])
print(*m,sep="\n")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# 주어진 범위 내에서 소수를 먼저 모두 구해놓고 범위를 제한
# num = []
# for i in range(2, 246913):
#     cnt = 0

#     for p in range(2, int(i**0.5)+1):
#         if i % p == 0:
#             cnt += 1
#             break
#     if cnt == 0:
#         num.append(i)
# while True:
#     n = int(input())
#     res = 0
#     if n == 0:
#         break
#     for i in num:
#         if n < i <= 2*n:
#             res += 1
#     print(res)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    
# 파이썬 제곱근 함수 sqrt
# math 라이브러리를 import 해주어야 사용이 가능
# from math import sqrt
# while True :
#   n = int(input())
#   if n == 0 :
#     break
#   result = 0
#   for i in range(n+1, 2*n + 1) :
#     if i == 1 :
#       continue
#     elif i == 2 :
#       result += 1
#       continue
#     else :
#       for j in range(2, int(sqrt(i) + 1)) :
#         if i % j == 0 :
#           break
#       else :
#         result += 1  
# print(result)
# -----------------------------------------------
# import math
# def IsPrime(num):
#     a = int(math.sqrt(num))
#     if num == 1:
#         return False
#     else:
#         for i in range(2, a+1):
#             if num % i == 0: 
#                 return False
#         return True
# while True:
#     n = int(input())
#     cnt = 0
#     if n == 0:
#          break
#     for i in range(n+1,2*n+1):
#         if IsPrime(i):
#              cnt += 1  
#     print(cnt)
# baekjoon 1929
L = []
a, b = map(int,input().split())
for i in range(a,b):
    if i != 1:
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            L.append(i)
print(*L,sep='\n')


# a, b = map(int,input().split())
# for i in range(a,b):
#     if i != 1:
#         for j in range(2,i):
#             if i % j == 0:
#                 break
#         else:
#             print(i)


# x, y = map(int, input().split())
# for i in range(x, y+1):
#     if i == 1: 
#         continue
#     for j in range(2, int(i** 0.5)+1 ):
#         if i%j==0:
#             break
#     else:
#         print(i)


# m, n = map(int, input().split())
# def prime_number(x) :
#   if x == 1 :
#     return False
#   else :
#     for i in range(2, int(x**0.5) + 1) :
#       if x % i == 0 :
#         return False
#     return True
# for i in range(m, n + 1) :
#   if prime_number(i) :
#     print(i)


# baekjoon 9020
import sys

prime_list = [False, False] + [True]*10002
#입력값은 10000까지 주어지며 0, 1번 인덱스는 False인 소수리스트를 만든다. 

for i in range(2, 10002):
    if prime_list[i]:
        for j in range(2*i, 10002, i):
        #소수를 구하기 위해 반복문을 돌린다. 10002보다 작지만 2의 배수들은 소수가 아니니 False값을 담는다. 
            prime_list[j] = False

T = int(sys.stdin.readline()) #입력받는 테스트 케이스의 개수 T

for i in range(T):
    n = int(sys.stdin.readline()) #입력받는 짝수 n
    a = n // 2 #입력받은 짝수의 중간값을 만들어 탐색한다.
    print(a)
    b = a
    while a > 0:
        if prime_list[a] and prime_list[b]:
        #a와 b가 소수일 때 True를 반환하므로 a, b를 출력한다.
            print(a, b)
            break
        else:
            a -= 1
            b += 1
            
# def Goldbach():
#     check = [False, False] + [True] * 10000
    
#     for i in range(2, 101):
#         if check[i] == True:
#             for j in range(i + i, 10001, i):
#                 check[j] = False

#     T = int(input())
#     for _ in range(T):
#         n = int(input())

#         A = n // 2
#         B = A
#         for _ in range(10000):
#             if check[A] and check[B]:
#                 print(A, B)
#                 break
#             A -= 1
#             B += 1

# Goldbach()

# import sys

# def prime(n):
#     prime_num = [True] * n
#     for i in range(2, int(n**0.5) + 1):
#         if prime_num[i] is True:
#             for j in range(2 * i, n, i):
#                 prime_num[j] = False
#     return [i for i in range(2, n) if prime_num[i] is True]


# p = prime(10001)  
# n = int(sys.stdin.readline())
# for i in range(n):
#     m = int(sys.stdin.readline())
#     diff = 10001
#     a = 0
#     b = 0
#     for i in range(len(p)):
#         if p[i] >= m / 2:  
#             if m - p[i] in p:
#                 a = p[i]
#                 b = m - p[i]
#                 break
#     print(b, a)

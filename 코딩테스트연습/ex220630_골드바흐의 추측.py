# baekjoon 9020
import sys

prime_list = [False, False] + [True]*10002
#�Է°��� 10000���� �־����� 0, 1�� �ε����� False�� �Ҽ�����Ʈ�� �����. 

for i in range(2, 10002):
    if prime_list[i]:
        for j in range(2*i, 10002, i):
        #�Ҽ��� ���ϱ� ���� �ݺ����� ������. 10002���� ������ 2�� ������� �Ҽ��� �ƴϴ� False���� ��´�. 
            prime_list[j] = False

T = int(sys.stdin.readline()) #�Է¹޴� �׽�Ʈ ���̽��� ���� T

for i in range(T):
    n = int(sys.stdin.readline()) #�Է¹޴� ¦�� n
    a = n // 2 #�Է¹��� ¦���� �߰����� ����� Ž���Ѵ�.
    print(a)
    b = a
    while a > 0:
        if prime_list[a] and prime_list[b]:
        #a�� b�� �Ҽ��� �� True�� ��ȯ�ϹǷ� a, b�� ����Ѵ�.
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
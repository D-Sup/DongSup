# 백준 10872번
import sys
N = int(sys.stdin.readline())
F = 1
for i in range(N,1,-1):
    F*=i
print(F)

# a=int(input())
# def factorial(i):
#     if i==0: return 1
#     return i*factorial(i-1)
# print(factorial(a))
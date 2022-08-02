# # 백준 10872번
# import sys
# N = int(sys.stdin.readline())
# F = 1
# for i in range(N,1,-1):
#     F*=i
# print(F)


def factorial(i):
    if i==0: 
        return True
    return i*factorial(i-1)
print(factorial(3))

# new method
def f(x):
    return (x * f(x-1)) if x else 1
print(f(3))
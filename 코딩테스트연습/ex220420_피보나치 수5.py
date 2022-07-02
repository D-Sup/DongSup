# 백준 10870번
def fibonacci(num):
    if num<=1:
        return num
    return fibonacci(num-1)+fibonacci(num-2)

n=int(input())
print(fibonacci(n))

# a = 0
# b = 1
# c = 1
# for _ in range(int(input())):
#     a = b
#     b = c
#     c = a + b  
# print(a)
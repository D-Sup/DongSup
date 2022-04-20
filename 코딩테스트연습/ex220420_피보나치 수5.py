# 백준 10870번
def fibonacci(num):
    if num<=1:
        return num
    return fibonacci(num-1)+fibonacci(num-2)

n=int(input())
print(fibonacci(n))
# programmers 12910
def solution(arr, divisor):
    L = [i for i in arr if i%divisor==0]
    return sorted([i for i in arr if i%divisor==0]) if L else [-1]
print(solution([3,2,6],10))

def solution(arr, divisor):
    return sorted([i for i in arr if i%divisor==0]) or [-1]
print(solution([3,2,6],10))
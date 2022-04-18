# 백준 14563번
T = int(input())
N = list(map(int, input().split()))
for n in N:
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    if sum == n:
        print('Perfect')
    elif sum > n:
        print('Abundant')
    else:
        print('Deficient')
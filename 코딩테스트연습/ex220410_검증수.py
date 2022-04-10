N = list(map(int, input().split()))
R = 0
for i in N:
    R += i*i
print(R % 10)
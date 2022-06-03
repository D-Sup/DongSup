# baek1978
k = int(input())
C = 0
M = list(map(int,input().split()))
for i in M:
    if i != 1:
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            C += 1
print(C)
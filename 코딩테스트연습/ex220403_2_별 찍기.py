# 백준 2443번
N = int(input())
for i in range(N+1):
    print(' '*(N-i)+'*'*i,end='')
    for j in range(N):
        if i-1 > j:
            print('*',end='')
    print()

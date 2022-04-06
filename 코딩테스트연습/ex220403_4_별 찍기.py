# 백준 2522번
N = int(input())
for l in range(N+1):
    print(' '*(N-l)+'*'*l)
for i in range(N):
    for j in range(N):
        if i >= j:
            print(' ',end='')
        else:
            print('*',end='')
    print()
# 백준 2523번
N = int(input())
for i in range(N-1):
    for j in range(N):
        if i >= j:
            print('*',end='')
        else:
            print(' ',end='')
    print()
for l in range(N):
    print('*'*(N-l)+' '*l)




    
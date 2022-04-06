# 백준 2446번
N = int(input())
for i in range(0,N):
    print(' '*i+'*'*((N-i)*2-1))
for j in range(1,N):
    print(' '*(N-j-1)+'*'*((j*2+1)))
    
# for j in range(N-1,0,-1):
#     print(' '*(j-1)+'*'*((N-j)*2+1))

    
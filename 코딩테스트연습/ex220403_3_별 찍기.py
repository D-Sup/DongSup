# 백준 2444번
N = int(input())
for i in range(N+1):
    print(' '*(N-i)+'*'*i,end='')
    for j in range(N):
        if i-1 > j:
            print('*',end='')
    print()
for i in range(N):
    for j in range(N):
        if i >= j:
            print(' ',end='') 
        else:
            print('*',end='')
    print('*'*((N-2)-i)+' '*i)
print()

    
    
    


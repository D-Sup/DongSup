# 백준 2444번
N = int(input())
for i in range(N):
    for j in range(N):
        if i > j:
            print(' ',end='') 
        else:
            print('*',end='')
    print('*'*((N-1)-i)+' '*i)
print()

    
    
    


# baekjoon 2581
M = int(input())
N = int(input())
R = []
for i in range(M, N+1):
    if i == 1: 
        continue
    for j in range(2, int(i** 0.5)+1 ):
        if i%j==0:
            break
    else:
        R.append(i)
if len(R)!=0:     
    print(sum(R),min(R),sep='\n')
else:
    print(-1)
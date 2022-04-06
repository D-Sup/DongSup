# 백준 10984번
T = int(input())
C, G = [], []
for _ in range(T):  
    N = int(input())
    C = [0]*T
    G = [0]*T
    for _ in range(N):
        a, b = map(float,input().split())
        C.append(int(a)),G.append(b)
    print(sum(C),sum(G)/float(N))
print()

    
    
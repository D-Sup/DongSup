n = int(input())
for _ in range(n):
    A, B = [], []
    p = int(input())
    for _ in range(p):
        C, name = map(str,input().split())
        A.append(int(C)), B.append(name)
    print(B[A.index(max(A))])
        

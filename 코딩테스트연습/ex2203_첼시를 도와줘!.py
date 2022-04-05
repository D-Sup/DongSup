# 백준 11098번
# https://foam-waiter-a0e.notion.site/a064e3d0be344a4582461bc47311fdd5
n = int(input())
for _ in range(n):
    A, B = [], []
    p = int(input())
    for _ in range(p):
        C, name = map(str,input().split())
        A.append(int(C)), B.append(name)
    print(B[A.index(max(A))])
        

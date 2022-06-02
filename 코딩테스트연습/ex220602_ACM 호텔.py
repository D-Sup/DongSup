#baekjoon 10250
for _ in range(int(input())):
    H, W, C = map(int,input().split())
    R = H * W
    M = [0 for i in range(R)] 
    N = [j for j in range(R)] 
    P = C // H 
    Q = C % H
    S = 0 
    for p in range(P): 
        if S > 100*H:
            S -= 100*H
        S += 1
        for q in N[p::W]:
            S += 100
            M[q] = S
    print(max(M)-(100*H)+(100*Q)+1)
    
# for i in range(int(input())):
#     H, W, C = map(int, input().split())
#     f, P = 0, 0
#     if C % H == 0:
#         f = H * 100
#         P = C // H
#     else:
#         f = (C % H) * 100
#         P = 1 + C // H
#     print(f + P)    

# for _ in range(int(input())):
#     H,W,N=map(int,input().split())
#     a=N%H;b=N//H+1
#     print(a, b ,sep=',')
#     if a==0 : a=H;b-=1
#
#     print(a*100+b)
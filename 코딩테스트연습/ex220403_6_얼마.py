# 백준 9325번
T=int(input())
q, p, h, v, f = [], [], [], [], []
for _ in range(T):
    S = int(input())
    h.append(S)
    N = int(input())
    for _ in range(N):
        a, b = map(int,input().split())
        q.append(a),p.append(b)
        v.append(q[-1]*p[-1])
    f.append(sum(h)+sum(v))
    h = [0] * T
    q = [0] * N
    p = [0] * N
    v = [0] * N
for i in range(T):
    print(f[i])


# T = int(input())
# for _ in range(T):
#     s = int(input())
#     n = int(input())
#     price = s
#     for _ in range(n):
#         q, p = map(int, input().split())
#         price += q * p
#     print(price)
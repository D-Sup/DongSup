# beakjoon 11050
N,K = map(int,input().split())

def solution(V):
    R = 1
    for i in range(1,V+1):
        R *= i
    return R

a = solution(N)
b = solution(N-K)
c = solution(K)

print(a // (c * b))
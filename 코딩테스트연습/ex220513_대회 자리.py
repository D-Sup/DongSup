# baekjoon 5176
import sys
input = sys.stdin.readline
N = int(input())
for _ in range(N):
    H = []
    a, b = map(int,input().split())
    for _ in range(a):
        H.append(int(input()))
        if max(H) > b:
            break
    print(len(H)-len(set(H)))
    del(H)
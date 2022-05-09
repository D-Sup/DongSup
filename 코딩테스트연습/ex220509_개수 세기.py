# baekjoon 10807
import sys
input = sys.stdin.readline
N = int(input())
M = list(map(int,input().split()))
V = int(input())
r = 0
for i in range(N):
    if M[i] == V:
        r += 1
print(r)
    

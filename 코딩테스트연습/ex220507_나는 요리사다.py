# baekjoon 2953번
import sys
input = sys.stdin.readline
max = 0
for i in range(1,6):
    N = list(map(int,input().split()))
    if max < sum(N):
        max = sum(N)
        j = i
print(j,max)
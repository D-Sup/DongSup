# baekjoon 2587
import sys, math
input = sys.stdin.readline
N = []
for _ in range(5):
    N.append(int(input()))
print(sum(N)//len(N))
N.sort()
print(N[math.ceil(len(N)/2.0)-1])

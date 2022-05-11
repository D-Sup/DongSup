# baekjoon 2752
import sys
input = sys.stdin.readline
N = list(map(int,input().split()))
N.sort()
for i in range(len(N)):
    print(N[i], end = ' ')
 
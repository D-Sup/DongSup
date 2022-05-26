# baekjoon 9086
import sys
input = sys.stdin.readline
N = [str(input()) for _ in range(int(input()))]
print(*[N[i][0] + N[i][-2] for i in range(len(N))],sep='\n')
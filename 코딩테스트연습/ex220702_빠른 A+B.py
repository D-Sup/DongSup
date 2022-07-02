# baekjoon 15552
import sys
input = sys.stdin.readline
N = [list(map(int,input().split())) for _ in range(int(input()))]
print(*[sum(N[i]) for i in range(len(N))],sep='\n')
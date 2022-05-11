# baekjoon 10818
import sys
input = sys.stdin.readline
N = int(input())
T = list(map(int,input().split()))
print(min(T),max(T),sep=' ')
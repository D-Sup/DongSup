# 백준 2490번
import sys
for _ in range(3):
    N = list(map(int,sys.stdin.readline().split()))
    if sum(N) == 3:
        print('A')
    elif sum(N) == 2:
        print('B')
    elif sum(N) == 1:
        print('C')
    elif sum(N) == 0:
        print('D')
    else:
        print('E')
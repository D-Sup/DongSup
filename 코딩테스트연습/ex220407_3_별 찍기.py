# 백준 10991번
import sys
N = int(sys.stdin.readline())
for i in range(1,N+1):
    print(' '*(N-i),end='')
    print('* '*(i))
    
# N = int(input())

# for i in range(1, N+1):
#     print(' '* (N-i), end = '')
#     for j in range(i): 
#         print('*', end = ' ')
#     print()
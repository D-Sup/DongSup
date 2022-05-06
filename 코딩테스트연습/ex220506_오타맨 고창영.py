# baekjoon 2711
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, string = input().split()
    n = int(n)
    print(string[:n-1]+string[n:])
    
# import sys
# T = int(sys.stdin.readline())
# for _ in range(T):
#     N, M = sys.stdin.readline().split()
#     result = ""
#     for i in range(len(M)):
#         if i == int(N)-1:
#             continue        
#         result += M[i]
#     print(result)s
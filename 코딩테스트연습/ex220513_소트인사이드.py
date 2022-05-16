# baekjoon 1427
import sys
input = sys.stdin.readline
M = []
N = list(str(input()))
del(N[-1])
for i in range(len(N)):
    M.append(int(N[i]))
M.sort(reverse=True)
for j in range(len(M)):
    print(M[j],end='')

# import sys
# input = sys.stdin.readline
# N = int(input())
# M = []
# for i in str(N):
#     M.append(i)
# M.sort(reverse=True)
# print("".join(M))

# N = input()
# N = [int(i) for i in N]
# M = sorted(N, reverse=True)
# for i in M :
#     print(i, end="")

# N = list(map(str,input()))
# N.sort(reverse=True)
# for i in N:
#     print(i,end='')
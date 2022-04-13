# 백준 2576번
import sys
S, M = 0, 100
N = []
for i in range(7):
    N.append(int(sys.stdin.readline()))
    if N[i] % 2 == 1:
        S += N[i]
        if M > N[i]:
            M = N[i]
if S == 0:
    print('-1')
else:
    print('%s\n%s' % (S,M))

# import sys
# input = sys.stdin.readline
# s = []
# for i in range(7):
#     a = int(input())
#     if a % 2 != 0: s.append(a)
# if s:
#     print(sum(s))
#     print(min(s))
# else:
#     print(-1)
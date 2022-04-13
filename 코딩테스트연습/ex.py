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
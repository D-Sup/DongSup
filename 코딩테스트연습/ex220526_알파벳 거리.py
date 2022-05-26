# baekjoon 5218
import sys
input = sys.stdin.readline
S = ''
N = [input().split() for _ in range(int(input()))]
for i in range((len(N))):
    M = [ord(N[i][1][j])-ord(N[i][0][j]) for j in range(len(N[i][0]))]
    for j in range(len(M)):
        if M[j] < 0:
            M[j] += 26
    M = " ".join(map(str,M))
    S += f'Distances: {M}\n'
print(S)
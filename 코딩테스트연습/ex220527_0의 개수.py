# baekjoon 11170
N = [input().split() for _ in range(int(input()))]
for i in range(len(N)):
    M = [str(j).count('0') for j in range(int(N[i][0]),int(N[i][1])+1)]
    print(sum(M))
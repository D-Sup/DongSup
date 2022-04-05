# 백준 2439번
n = int(input())
for i in range(n):
    for j in range(n):
        if i>=j:
            print('*', end = ' ')
    print()
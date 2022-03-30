# import sys
n = int(input())
info = []
for _ in range(n):
    info.append(input().split())
    # info.append(list(map(str,input().strip().split())))
    # info.append(input().strip().split())
#info.sort(key = lambda x: (int(x[1]), int(x[2]), int(x[3])))
info = sorted(info, key = lambda x: (int(x[1]), int(x[2]), int(x[3])))
print(info[0][0])
print(info[-1][0])
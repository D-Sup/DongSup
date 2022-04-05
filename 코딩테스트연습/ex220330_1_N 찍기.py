# 백준 2741번
# import sys
n = int(input())
info = []
for _ in range(n):
    #생년월일 정수형으로 변환 위해 임시로 저장
    info.append(input().split())
    # info.append(list(map(str,input().strip().split())))
    # info.append(input().strip().split())
info.sort(key = lambda x: (int(x[1]), int(x[2]), int(x[3])))
#info = sorted(info, key = lambda x: (int(x[1]), int(x[2]), int(x[3])))
print(info[0][0])
print(info[-1][0])
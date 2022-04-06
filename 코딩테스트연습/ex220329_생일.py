# 백준 5635번
# https://foam-waiter-a0e.notion.site/7929c2d1040b43209474eb443a8a946c
n = int(input())
for _ in range(n):
    p = int(input())
    player = []
    for _ in range(p):
        player.append(input().strip().split())
    player.sort(key=lambda x:int(x[0]), reverse=True)
    print(player[0][1])
    
# # import sys
# n = int(input())
# info = []
# for _ in range(n):
#     #생년월일 정수형으로 변환 위해 임시로 저장
#     info.append(input().split())
#     # info.append(list(map(str,input().strip().split())))
#     # info.append(input().strip().split())
# info.sort(key = lambda x: (int(x[1]), int(x[2]), int(x[3])))
# #info = sorted(info, key = lambda x: (int(x[1]), int(x[2]), int(x[3])))
# print(info[0][0])
# print(info[-1][0])
   
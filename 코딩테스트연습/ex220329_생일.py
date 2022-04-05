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
   
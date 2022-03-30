n = int(input())
for _ in range(n):
    p = int(input())
    player = []
    for _ in range(p):
        player.append(input().strip().split())
    player.sort(key=lambda x:int(x[0]), reverse=True)
    print(player[0][1])
   
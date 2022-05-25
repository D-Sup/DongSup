T = int(input())
for _ in range(T) :
  N = int(input())
  C = G = 0
  for i in range(N) :
    c, g = map(str, input().split())
    C += int(c)
    G += float(c) * float(g)

  result = round(G / C, 1)
  print(C, result)

# for _ in range(int(input())):
#     C = G = 0
#     for i in range(int(input())):
#         c, g = map(float, input().split())
#         C += c
#         G += c*g
#     print("%d %.1f" %(C, G/C))
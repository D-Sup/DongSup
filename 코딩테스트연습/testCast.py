L = []
for i in range(1,9):
    for j in range(1,9):
        L.append([i,j])

N = str(input())
B = ['a','b','c','d','e','f','g','h']
b = B.index(N[0])+1 # 3
a = int(N[1]) # 2
MOVECASE = [[-1,-2] , [-1,+2] , [+1,-2] , [+1,+2], [+2,-1] , [+2,+1], [-2,-1] , [-2,+1]]

count = 0
for p in range(len(MOVECASE)):
    c = a + MOVECASE[p][0]
    d = b + MOVECASE[p][1]
    for i in L:
        if i in [[c,d]]:
            count += 1
print(count) #6

# L = [[1,2],[2,3]]

# for i in L:
#     if i in [[1,2]]:
#         print("yes")

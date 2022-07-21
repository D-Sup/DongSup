# [구현] 왕실의 나이트 

# 내 풀이
# [2,3] 에 있을 때 이동할 수 있는 곳
# [1,1]   ,  [1,5]  ,  [3,1]  ,  [3,5] , [4,2]   , [4,4]
# [-1,-2] , [-1,+2] , [+1,+2] , [+1,+2], [+2,-1] , [+2,+1] , + [-2,-1] , [-2,+1]
N = str(input())
B = ['a','b','c','d','e','f','g','h']
b = B.index(N[0])+1 # 3
a = int(N[1]) # 2
MOVECASE = [[-1,-2] , [-1,+2] , [+1,-2] , [+1,+2], [+2,-1] , [+2,+1], [-2,-1] , [-2,+1]]

count = 0
for p in range(len(MOVECASE)):
    c = a + MOVECASE[p][0]
    d = b + MOVECASE[p][1]
    count += 1
    if c < 1 or c > 8 or d < 1 or d > 8:
        count -= 1
print(count) #6


# 내 풀이 2
# 실제로 체스판의 크기만큼 리스트를 만들어서 풀기
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


# 답안
# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
# 2차원 배열을 이용한 방향 벡터 정의 >> dx, dy를 이용하지 않아도 된다.
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1),
         (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)


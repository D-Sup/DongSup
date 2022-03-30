# 어떤 반에 있는 학생들의 생일이 주어졌을 때, 가장 나이가 적은 사람과 가장 많은 사람을 구하는 프로그램을 작성하시오.

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
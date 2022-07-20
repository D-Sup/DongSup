# [구현] 시각

# 내 풀이 
N = int(input())
result = []
H = 0
for hour in range(N+1):
    for minute in range(60):
        for second in range(60):
            result = [hour,minute,second]
            for _ in range(3):
                result.extend([result[0]//10,result[0]%10])
                del(result[0])
            if result.count(3) >= 1:
                H += 1                 
print(H)

# 답안
# H를 입력받기
h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)
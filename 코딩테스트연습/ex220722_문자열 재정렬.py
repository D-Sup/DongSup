# [구현] 문자열 재정렬

# 내 풀이 
N = list(str(input()))
L, result = [], []
for i in range(len(N)):
    for j in range(1,10):
        if N[i] == str(j):
            L.append(N[i])
            H = [int(X) for X in L]
for q in L[::-1]:
    del(N[N.index(q)])            
for p in N:
    result.append(ord(p))
result.sort()
for Y in range(len(result)):
    result[Y] = chr(result[Y])
print(*result,sep='',end='')
print(sum(H))


# 답안 
data = input()
result = []
value = 0
# 문자를 하나씩 확인하며
for x in data:
    # 알파벳인 경우 결과 리스트에 삽입
    if x.isalpha():
        result.append(x)
    # 숫자는 따로 더하기
    else:
        value += int(x)
# 알파벳을 오름차순으로 정렬
result.sort()
# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
    result.append(str(value))
# 최종 결과 출력(리스트를 문자열로 변환하여 출력)
print(''.join(result))
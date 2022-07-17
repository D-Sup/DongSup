# 곱하기 혹은 더하기
# 두 수에 대해 연산을 수행
# 1이하인 경우 더하기 아닌 경우 곱하기하여 만들어질 수 있는 가장 큰 수 
data = list(map(int,(str(input()))))
result = 0
for i in data:
    if i <= 1 or result == 0:
        result += i
    else:
        result *= i
print(result)
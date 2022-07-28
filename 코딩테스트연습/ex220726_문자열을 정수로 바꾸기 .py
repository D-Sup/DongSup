# programmers 12925
L = []
def solution(s):
    for i in str(s):
        if i.isdigit():
            L.append(int(i))
        else:
            if i == "-":
                L.append(i)
    return L
print(*solution("-1234"),sep='')

# def solution(s):
#     return s
# print("-1234")

# def strToInt(str):
#     result = 0
#     for idx, number in enumerate(str[::-1]):
#         if number == '-':
#             result *= -1
#         else:
#             result += int(number) * (10 ** idx)
#     return result
# print(strToInt("-1234"));
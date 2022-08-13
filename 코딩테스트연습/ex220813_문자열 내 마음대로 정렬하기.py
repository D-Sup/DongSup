# programmers 12915
# 사전순 구현 x
def solution(strings, n):
    r = 0
    x = {}
    for i in strings:
        x[r] = i
        r+=1
    for key, value in x.items():
        x[key]=value[n] # 딕셔너리에 데이터 추가, 두번째 문자만 추출
    R = sorted(x.items(), key=lambda x: x[1]) # 두번째(키가 아닌 value) 기준으로 정렬
    print(R)
    S = []
    for j in range(len(R)):
        S.append(strings[R[j][0]])
    return S
print(solution(["abce", "abcd", "cdx"],2))

# def solution(strings, n):
#     return sorted(strings,key = lambda x: (x[n], x))
# 사전순으로 정렬하고 싶을경우 뒤에 x를 하나 더 붙여줌

# def solution(strings, n):
#     new = []
#     for i in strings:
#         new.append(i[n]+i)
#     new.sort()
#     answer =[]
#     for i in new:
#         answer.append(i[1:])
#     return answer
# print(solution(["abce", "abcd", "cdx"],2))
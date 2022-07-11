# programmers 12930
def solution(s):
    answer = ''
    R = s.split(' ')
    for p in R:
        for q in range(len(p)):
            if q % 2 == 0:
                answer += p[q].upper()
            else:
                answer += p[q].lower()
        answer += ' '
    return answer[0:-1]
print(solution("try hello world"))

# def toWeirdCase(s):
#     return ' '.join([''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(w)]) for w in s.split()])
# print("결과 : {}".format(toWeirdCase("try hello world")))

# def toWeirdCase(s):
#     return " ".join(map(lambda x: ''.join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))
# print("결과 : {}".format(toWeirdCase("try hello world")))

# programmers 12903
def solution(s):
    return s[len(s)//2-1:len(s)//2+1] if len(s) % 2 == 0 else s[len(s)//2]
print(solution("qwerr"))

def solution(str):
    return str[(len(str)-1)//2:len(str)//2+1]
print(solution("qwerr"))
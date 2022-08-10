# programmers 12917
def solution(s):
    L = sorted([ord(i) for i in s],reverse=True)
    s =''
    for k in L:
        s+=chr(k)
    return s
print(solution("Zbcdefg"))

def solution(s):
    return ''.join([chr(n) for n in sorted([ord(c) for c in s], reverse=True)])
print(solution("Zbcdefg"))

def solution(s):
    return ''.join(sorted(s,reverse=True))
print(solution("Zbcdefg"))
# programmers 12916
def solution(s):
    return True if s.count('P')+s.count('p') == s.count('Y')+s.count('y') else False
print(solution("pPoooyY"))

def solution(s):
    return s.lower().count('p') == s.lower().count('y')
print(solution("pPoooyY"))

from collections import Counter
def solution(s):
    r = Counter(s.lower())
    return r['p'] == r['y']
print(solution("pPoooyY"))



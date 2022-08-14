# programmers 12906
# 런타임 error 
def solution(arr):
    r=0
    for i in range(len(arr)):
        if arr[i]==r:
            r=arr[i]
            arr[i]='D'
            continue
        r=arr[i]
    for _ in range(arr.count('D')):
        arr.remove('D')
    return arr
print(solution([4,4,4,3,3]))

# ------------------------------------------

def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(1, len(arr)):  
        if arr[i-1] != arr[i]:
          answer.append(arr[i])
    return answer
print(solution([4,4,4,3,3]))

def solution(s):
    a = []
    for i in s:
        if a[-1:] == [i]: 
            continue
        a.append(i)
    return a
# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution([4,4,4,3,3]))

# ------------------------------------------

def solution(s):
    s = ''.join(str(i) for i in s)
    return [int(s[i]) for i in range(len(s)) if s[i] != s[i+1:i+2]]
print(solution([4,4,4,3,3]))


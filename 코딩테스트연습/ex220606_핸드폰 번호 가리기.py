# programmers 12948
def solution(ans):
    for i in range(len(ans[:-4])):
        ans[i] = '*'
    print(*ans)
solution(list(input()))
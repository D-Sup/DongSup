# # programmers 12948
# def solution(ans):
#     for i in range(len(ans[:-4])):
#         ans[i] = '*'
#     print(*ans)
# solution(list(input()))

# def solution(ans):
#     for i in range(len(ans)-4):
#         ans=ans.replace(ans[i],'*',1)
#     return ans
# print(solution('01075675023'))

def solution(ans):
    return "*"*(len(ans)-4) + ans[-4:]
print(solution('01075675023'))

# def solution(ans):
#     return "*"*len(ans[:-4])+ans[-4:]
# print(solution('01075675023'))


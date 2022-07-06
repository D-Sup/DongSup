# programmers 12935
def solution(arr):
    answer = arr
    if answer[0] == 10:
        answer.clear(),answer.append(-1)
        return answer
    del(answer[answer.index(min(answer))])
    return answer
print(solution([4,3,2]))

# def solution(answer):
#     if answer[0] == 10:
#         answer.clear(),answer.append(-1)
#         return answer
#     return [i for i in answer if i > min(answer)]
# my_list = [10]
# print("결과 {} ".format(solution(my_list)))
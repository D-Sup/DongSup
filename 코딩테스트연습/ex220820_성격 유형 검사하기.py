# programmers 118666
case = ["R","T","C","F","J","M","A","N"]
score_case = [3,2,1,0,1,2,3]
K = [0,0,0,0,1,1,1]

def solution(survey,choices):
    count = [0] * 8 
    score = [score_case[i-1] for i in choices]
    Q = [survey[i][K[choices[i]-1]] for i in range(len(choices))]
    for x in range(len(Q)):
        count[case.index(Q[x])] = score[x]
    R = []
    a = 0
    for _ in range(4):
        if count[a] < count[a+1]:
            c = 1
        else:
            c = 0
        R.append(case[a:a+2][c])
        a+=2 
    return R
print(solution(["TR", "RT", "TR"],[7,1,3]))


from collections import defaultdict

def solution(survey, choices):
    scores = defaultdict(int) 
    for (first, second), choice in zip(survey, choices):
        survey_choice = first if choice < 4 else second # 고른 선택지의 번호에 따라 유형의 알파벳이 무엇인지 
        scores[survey_choice] += abs(4 - choice) # 그 알파벳에 대한 점수를 합산 

    answer = ""
    for first, second in ("RT", "CF", "JM", "AN"): # scores = defaultdict(int)  점수가 아예 없는 유형은 자동으로 디폴트값이 0이 되도록 
        answer += first if scores[second] < scores[first] \
            else second if scores[first] < scores[second] \
            else min(first, second)
    return answer

if __name__ == '__main__':
    result = solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5])
    print("TCMA" == result, result)

    result = solution(["TR", "RT", "TR"], [7, 1, 3])
    print("RCJA" == result, result)
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


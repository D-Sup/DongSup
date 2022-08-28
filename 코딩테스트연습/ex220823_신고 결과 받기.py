### 1 ###
from collections import defaultdict

def solution(id_list, report,k):
    answer = []
    # 중복 신고 제거
    report = list(set(report))
    print(report)
    # user별 신고한 id 저장
    user = defaultdict(set)
    # user별 신고당한 횟수 저장
    cnt = defaultdict(int)
	
    for r in report:
        # report의 첫번째 값은 신고자id, 두번째 값은 신고당한 id
        a,b = r.split()
        # 신고자가 신고한 id 추가
        user[a].add(b)
    
        # 신고당한 id의 신고 횟수 추가
        cnt[b] += 1

    for i in id_list:
        result = 0
        # user가 신고한 id가 k번 이상 신고 당했으면, 받을 메일 추가
        for u in user[i]: # 신고한 id
            if cnt[u]>=k: # 신고당한 id의 횟수
                result +=1
        answer.append(result) # k번 이상이면 신고자 id의 위치에 카운터
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2))

### 2 ###
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {x:0 for x in id_list}
    for i in set(report):
        reports[i.split()[1]] += 1 # id 마다 신고한 id의 갯수 저장 
    for j in set(report):
        result = 0
        if reports[j.split()[1]] >= k:
            answer[id_list.index(j.split()[0])] += 1
        
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2))

### 3 ###
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    dic_report = {id: [] for id in id_list} # 해당 유저를 신고한 ID
    for i in set(report):
        i = i.split()
        dic_report[i[1]].append(i[0]) # 반대로 해당아이디를 신고한 id를 저장
    print(dic_report)
    for key, value in dic_report.items():
        if len(value) >= k:
            for j in value:
                answer[id_list.index(j)] += 1

    return answer

print(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2))



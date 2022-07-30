# prgrammers 12922
def solution(s):
    return s//2*"수박" + s%2*"수"
print(solution(int(input())))

# def solution(n):
#     return "".join(["수박"[i%2] for i in range(n)])
# print(solution(int(input())))

# def solution(n):
#     return ("수박"*n)[:n]
# print(solution(int(input()))) 
# programmers 12940
def solution(n, m):
    answer = []
    # 최대 공약수
    v = min(n, m)
    for i in range(v, 0, -1) :
        if n % i == 0 and m % i == 0 :
            answer.append(i)
            break
    # 최소 공배수
    v = max(n, m)
    for i in range(v, v * v) :
        if i % n == 0 and i % m == 0 :
            answer.append(i)
            break
    return answer
print(solution(3,12))

# def gcd(a, b):
#     return b if a % b == 0 else gcd(b, a % b)
# # 나머지가 0일 때, b값으로 True
# def lcm(a, b):
#     return int(a * b / gcd(a, b))
# # 최소공배수 = a*b / 최대공약수 
# def gcdlcm(a, b):
#     answer = [gcd(a,b), lcm(a,b)]
#     return answer
# print(gcdlcm(3,12))

# def gcdlcm(a, b):
#     c, d = max(a, b), min(a, b)
#     t = 1
#     while t > 0:
#         t = c % d
#         c, d = d, t
#     answer = [c, int(a*b/c)]
#     return answer
# print(gcdlcm(3,12))
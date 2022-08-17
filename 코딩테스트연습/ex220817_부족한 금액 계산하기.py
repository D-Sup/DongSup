# programmers 82612
def solution(price,money,count):
    Hap = 0
    for i in range(1,count+1):
        Hap += price*i
        result = Hap - money
    return result if result>0 else 0
print(solution(3,20,4))

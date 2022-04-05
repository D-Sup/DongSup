# 백준 10984번
s = []
while 1:
    a, b = map(int,input().split())
    s.append(a+b)
    if s[-1] == 0:
        del(s[-1])
        break
for i in s:
    print(i)
    
    